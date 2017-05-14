#!/usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import find_packages, setup

from {{cookiecutter.pkg_name}} import __version__

setup(
    name='{{cookiecutter.pkg_name}}',
    version=__version__,
    license='PRIVATE',
    author='',
    author_email='',
    description='',
    packages=find_packages(exclude=['tests']),
    zip_safe=False,
    install_requires=[
        'tornado',
        'gevent',
        'tracing.config'
    ],
    entry_points={
        'console_scripts': [
        ],
    }
)
