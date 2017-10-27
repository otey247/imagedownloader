#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from setuptools import setup, find_packages

"""
Bulk image downloader from a list of urls
"""

# Get the long description from the README file
readme_file = Path(__file__).parent / 'README.md'
with readme_file.open(encoding='utf-8') as f:
    long_description = f.read()


about = {}
about_file = list(Path().glob('./**/__about__.py'))[0]
with about_file.open() as f:
    exec(f.read(), about)

setup(
    name=about["__title__"],
    version=about['__version__'],
    description=about['__description__'],
    author=about["__author__"],
    author_email=about["__email__"],
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    entry_points={'console_scripts': ['imgdownloader=imagedownloader.cli:main']},
    install_requires=[
        'Pillow>=4.2.1',
        'requests>=2.14.2',
        'six>=1.10',
        'tqdm>=4.15.0',
        'PyYAML',
    ],
    extras_require={
        'dev': [
            'jupyter',
            'ipython',
            'pandas'
        ],
    },
    long_description=long_description,
    zip_safe=False
)
