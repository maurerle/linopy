#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module aims at testing the correct behavior of the Variables class.
"""

import numpy as np
import pandas as pd
import pytest

import linopy
from linopy import Model


@pytest.fixture
def m():
    m = Model()
    m.add_variables(coords=[pd.RangeIndex(10, name="first")], name="x")
    m.add_variables(coords=[pd.Index([1, 2, 3], name="second")], name="y")
    m.add_variables(0, 10, name="z")
    return m


def test_variables_repr(m):
    m.variables.__repr__()


def test_variables_assignment_with_merge():
    """
    Test the merger of a variables with same dimension name but with different
    lengths.

    Missing values should be filled up with -1.
    """
    m = Model()

    upper = pd.Series(np.ones((10)))
    m.add_variables(upper)

    upper = pd.Series(np.ones((12)))
    m.add_variables(upper)
    assert m.variables.labels.var0[-1].item() == -1


def test_scalar_variables_name_counter():
    m = Model()
    m.add_variables()
    m.add_variables()
    assert "var0" in m.variables
    assert "var1" in m.variables


def test_variables_binaries(m):
    assert isinstance(m.binaries, linopy.variables.Variables)


def test_variables_nvars(m):
    assert m.variables.nvars == 14

    idx = pd.RangeIndex(10, name="first")
    mask = pd.Series([True] * 5 + [False] * 5, idx)
    m.add_variables(coords=[idx], mask=mask)
    assert m.variables.nvars == 19


def test_variables_get_name_by_label(m):
    assert m.variables.get_name_by_label(4) == "x"
    assert m.variables.get_name_by_label(12) == "y"

    with pytest.raises(ValueError):
        m.variables.get_name_by_label(30)

    with pytest.raises(ValueError):
        m.variables.get_name_by_label("anystring")
