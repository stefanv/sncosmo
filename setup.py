#!/usr/bin/env python
# Licensed under a 3-clause BSD style license - see LICENSE.rst

import numpy
from Cython.Build import cythonize
import os
import re

from setuptools import setup
from setuptools.extension import Extension

# Extensions
source_files = [os.path.join("sncosmo", "salt2utils.pyx")]
include_dirs = [numpy.get_include()]
extensions = [Extension("sncosmo.salt2utils", source_files,
                        include_dirs=include_dirs)]
extensions = cythonize(extensions)

# Synchronize version from code.
VERSION = re.findall(r"__version__ = \"(.*?)\"",
                     open(os.path.join("sncosmo", "__init__.py")).read())[0]

setup(version=VERSION, ext_modules=extensions)
