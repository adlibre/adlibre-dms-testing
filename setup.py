#!/usr/bin/env python

from setuptools import setup

setup(name='dms_testing',
    version='0.1.1',
    long_description=open('README.md').read(),
    url='https://github.com/macropin/adlibre-dms-testing',
    packages=['dms_testing',],
    install_requires=['django','django_lorem_pdf', 'rng'],
#    package_data={ 'lorem_pdf': ['templates/*',] },
    dependency_links = [
        "https://github.com/macropin/django-lorem-pdf/tarball/master#egg=django_lorem_pdf",
	"https://github.com/macropin/random-name-generator/tarball/master#egg=rng",
    ],
)
