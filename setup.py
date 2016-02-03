#!/usr/bin/env python
# -*- conding=utf-8 -*-

from distutils.core import setup

setup(name='simple_log',
    version='0.0.1',
    author='Christos Mantas',
    author_email='the1pro@gmail.com',
    url='http://github.com/cmantas/simple_log',
    license='http://www.apache.org/licenses/LICENSE-2.0.html',
    description='Simplistic wrapper for Python logging module',
    long_description=open('README.md').read(),
    packages=['simple_log'],
    zip_safe=False)