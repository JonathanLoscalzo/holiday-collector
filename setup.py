#!/usr/bin/env python
import setuptools
from setuptools import find_packages


def get_version(filename):
    with open(filename) as in_fh:
        for line in in_fh:
            if line.startswith('__version__'):
                return line.split('=')[1].strip()[1:-1]
    raise ValueError("Cannot extract version from %s" % filename)


setuptools.setup(
    name="holidaycollector",
    version=get_version("holidaycollector/holidaycollector.py"),
    url="https://github.com/goerz/holidaycollector",
    author="Jonathan Loscalzo",
    author_email="jonathan.r.loscalzo@gmail.com",
    description="an script that collects and parse ics files to csv or others",
    packages = find_packages(exclude=('tests', 'docs')),
    install_requires=[
        'Click',
    ],
    # extras_require={'dev': ['pytest',]},
    # py_modules=['holidaycollector'],
    entry_points='''
        [console_scripts]
        holidaycollector=holidaycollector.holidaycollector:main
    ''',
    classifiers=[
        'Environment :: Console',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
