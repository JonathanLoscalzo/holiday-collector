#!/usr/bin/env python
"""an script that collects and parse ics files to csv or others"""
# See LICENSE for terms of use.

import sys
import logging

import click
import readline  # this import is needed because of misunderstood of arrowkeys when promp
import os
import pandas as pd
from holidaycollector.tasks.download_ics import download
from holidaycollector.tasks.transform_csv import transform

__version__ = "0.0.1"


def set_config(debug: bool):
    logging.basicConfig(level=logging.WARNING)
    logger = logging.getLogger(__name__)
    if debug:
        logger.setLevel(logging.DEBUG)
        logger.debug("Enabled debug output")
    return logger


# @click.command()
@click.help_option("--help", "-h")
@click.version_option(version=__version__)
@click.option("--debug", is_flag=True, help="enable debug logging")
@click.group("holiday collector")
def main(debug=True):
    """an script that collects and parse ics files to csv or others"""
    pass


@main.command()
@click.argument("country")
def download_ics(country):
    filename = download(country)
    click.echo(f"Downloaded file at: {filename}")
    return filename


@main.command()
@click.argument("filename")
def transform_csv(filename):
    try:
        csv_filename = transform(filename)
        click.echo(f"Parsed file at: {csv_filename}")
    except FileNotFoundError as e:
        click.echo("Archivo no encontrado")


@main.command()
@click.argument("country")
def download_and_transform(country):
    filename = download(country)
    filename = filename.split("/")[-1]
    transform(filename)
    # transform_csv(filename)


@main.command()
@click.option(
    "--date-part",
    type=click.STRING,
    prompt=True,
    help="Ingrese la fecha en formato yyyymm",
)
def concat_files(date_part):
    files = []
    countries = []

    while True:
        country = click.prompt(
            "Seleccione un país",
            type=click.Choice(["colombia", "argentina", "uruguay"]),
        )

        countries.append(country)

        if not click.confirm("¿Desea agregar otro país?"):
            break

    click.echo(f"Paises seleccionados: {countries}")
    click.echo(f"Los archivos serán del formato {date_part}_<pais>.csv...")

    for country in countries:
        filepath = f"./data/csv/{date_part}_{country}.csv"
        if not (os.path.exists(filepath) and os.path.isfile(filepath)):
            click.echo(f"El archivo {filepath} no existe, intente nuevamente")
            continue

        files.append(filepath)

    if len(files) == 0:
        return click.echo("No existe ningún archivo, intente nuevamente")
    df = pd.concat([pd.read_csv(f) for f in files], ignore_index=True).sort_values(
        by=["date"]
    )

    df.to_csv("./data/2021-holidays.csv", index=False)


if __name__ == "__main__":
    main()