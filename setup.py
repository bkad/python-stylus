#!/usr/bin/env python
from setuptools import setup
import io
import sys

with io.open('README.md') as description_file:
  long_description = description_file.read()

setup(
    name="stylus",
    version="0.1.0",
    author="Kevin Le",
    description="A bridge to the Stylus css compiler",
    packages=["stylus"],
    package_dir={"stylus": "stylus"},
    package_data={
      "stylus": ["runner.js", "compiler.js"]
    },
    long_description=long_description,
    url="https://github.com/bkad/python-stylus",
    author_email="solnovus@gmail.com",
    license="MIT License",
    classifiers=[
      "Development Status :: 3 - Alpha",
      "Programming Language :: Python :: 2",
      "Programming Language :: Python :: 2.7",
    ],
    install_requires=["PyExecJs"]
)

