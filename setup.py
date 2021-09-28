# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='f1-telemetry-simulator',
    version='0.1.0',
    description='Package for F1 Telemetry (currently 2021 only)',
    long_description=readme,
    author='Patrick Jain-Taylor',
    author_email='patrick.andrew.taylor@gmail.com',
    url='https://github.com/patrick-andrew-jain-taylor/f1-telemetry-simulator',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
