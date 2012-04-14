#!/usr/bin/env python

from setuptools import setup

setup(name='dms_testing',
    version='0.1.0',
    long_description=open('README.md').read(),
    url='https://github.com/macropin/adlibre-dms-testing',
    packages=['dms_testing',],
    install_requires=['django','lorem_pdf', 'rng'],
    package_data={ 'lorem_pdf': ['templates/*',] },
    dependency_links = [
        "https://github.com/macropin/django-lorem-pdf/tarball/master#egg=lorem_pdf",
	"https://github.com/macropin/random-name-generator/tarball/master#egg=rng",
    ],
)
