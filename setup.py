#!/usr/bin/env python
# setup.py

from setuptools import setup

setup(
    name='Django CMS with Markdown Support',
    version='0.1',
    author='Cyrille Mescam',
    author_email='cmescam@gmail.com',
    url='https://github.com/datiti/django-cms',
    setup_requires=['setuptools-markdown'],
    long_description_markdown_filename='README.md',
)
