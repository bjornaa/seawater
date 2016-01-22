#!/usr/bin/env python
# --- encoding: iso-8859-1 ---

# ------------------------------------
# setup-file for the seawater package
# Bjørn Ådlandsvik, <bjorn@imr.no>
# 07 November 2004
# ------------------------------------

from distutils.core import setup

setup(name         = 'seawater',
      version      = '1.1',
      description  = 'Functions for physical properties of sea water',
      author       = 'Bjørn Ådlandsvik',
      author_email = 'bjorn@imr.no',
      url          = 'http://www.imr.no/~bjorn/python/seawater/',
      packages     = ['seawater']
      )
      
