#!/usr/bin/env python

from setuptools import setup

setup(name='dms_testing',
    version='0.1.2',
    long_description=open('README.md').read(),
    url='https://github.com/macropin/adlibre-dms-testing',
    packages=['dms_testing',],
    install_requires=['django', 'lorem_pdf', 'random_name_generator'],
    dependency_links = [
        "https://github.com/macropin/django-lorem-pdf/tarball/master#egg=lorem-pdf",
	"https://github.com/macropin/random-name-generator/tarball/master#egg=random-name-generator",
    ],
)
