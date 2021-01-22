"""Collection of tests for holidaycollector.py"""
import click

from click.testing import CliRunner
# from distutils.version import LooseVersion
from holidaycollector import main, __version__


# def test_version():
#     """Ensure that --version shows a version number that matches the
#     __version__ defined in the module, and is parsable by LooseVersion"""
#     runner = CliRunner()
#     result = runner.invoke(main, args=['--version'])
#     assert result.exit_code == 0
#     version = result.output.split()[-1]
#     assert version == __version__
#     assert LooseVersion(version) >= LooseVersion('0.0.1')


# def test_help():
#     """Ensure that -h and --help display the help"""
#     runner = CliRunner()
#     result = runner.invoke(main, args=['-h'])
#     result2 = runner.invoke(main, args=['--help'])
#     assert result.exit_code == 0
#     assert result.output.startswith("Usage:")
#     assert result.output == result2.output

def test_download_file():
    runner = CliRunner()
    result = runner.invoke(main, args=["download-ics", "germany"])
    assert result.exit_code == 0
    assert "germany.ics" in result.output

def test_transform_file():
    pass

def test_concat_files():
    pass

