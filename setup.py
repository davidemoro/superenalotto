#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import (
    setup,
    find_packages,
)


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


install_requires = [
    'reportlab',
]

tests_require = [
    'pytest',
]

setup(
    name='superenalotto',
    version='0.0.1.dev0',
    author='Davide Moro',
    author_email='davide.moro@gmail.com',
    maintainer='Davide Moro',
    maintainer_email='davide.moro@gmail.com',
    license='Apache Software License 2.0',
    url='https://github.com/davidemoro/superenalotto',
    description='stampa schedine superenalotto',
    long_description=open("README.rst").read() + "\n" +
    open("CHANGES.rst").read(),
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    classifiers=[
    ],
    extras_require={
        'tests': tests_require,
    },
)
