#!/usr/bin/env python
# --- coding: utf-8 ---

# ------------------------------------
# setup-file for the seawater package
# Bjørn Ådlandsvik, <bjorn@imr.no>
# 07 November 2004
# ------------------------------------

from distutils.core import setup

setup(
    name="seawater",
    version="1.3",
    description="Functions for physical properties of sea water",
    author="Bjørn Ådlandsvik",
    author_email="bjorn@imr.no",
    url="https://github.com/bjornaa/seawater.git",
    packages=["seawater"],
)
