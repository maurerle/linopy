#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 11:03:06 2021.

@author: fabulous
"""

# Note: For intercepting multiplications between xarray dataarrays, Variables and Expressions
# we need to extend their __mul__ functions with a quick special case
import linopy.monkey_patch_xarray
from linopy import model, remote
from linopy.expressions import merge
from linopy.io import read_netcdf
from linopy.model import LinearExpression, Model, Variable, available_solvers
from linopy.remote import RemoteHandler
from linopy.version import version as __version__
