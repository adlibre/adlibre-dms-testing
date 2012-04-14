#!/usr/bin/env python

from setuptools import setup

setup(name='dms_testing',
    version='0.1.4',
    long_description=open('README.md').read(),
    url='https://github.com/macropin/adlibre-dms-testing',
    packages=['dmstest'],
    scripts=['manage.py',],
    install_requires=['django==1.4', 'lorem_pdf', 'random_name_generator'],
    dependency_links = [
        "https://github.com/macropin/django-lorem-pdf/tarball/master#egg=lorem-pdf",
        "https://github.com/macropin/random-name-generator/tarball/master#egg=random-name-generator",
    ],
)
