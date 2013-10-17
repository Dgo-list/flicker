#!/usr/bin/env python

from setuptools import setup, find_packages


version = '0.0.1'

setup(
    name="flicker",
    version=version,
    packages=find_packages(),
    zip_safe=False,
    description="Flicker adds some logging utilities that improve on Django's defaults.",
    long_description="""\
""",
    classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='',
    author_email='',
    dependency_links=[
    ],
    url='',
    license='BSD',
    include_package_data=True,
    install_requires=[
    ],
    entry_points="""
    # -*- Entry points: -*-
    """,
)
