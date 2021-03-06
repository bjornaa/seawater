#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Simple test script for the seawater package

Test the functions against standard values in the
UNESCO 1983 report.

UNESCO 1983
N.P. Fofonoff and R.C. Millard Jr.,
Algorithms for computation of fundamental properties of seawater,
Unesco technical papers in marine science, 44.

Bjørn Ådlandsvik, <bjorn@imr.no>, 07 November 2004

"""

from __future__ import print_function

from seawater import *

format1 = "Computed: %25s = "
format2 = "Check value                         = "

print()
# Check value from UNESCO 1983, p. 20
print("Checking svan")
print()
print("S = 40, T = 40°C, P = 10000 dbar")
print(format1 % "svan(40, 40, 10000)", svan(40, 40, 10000))
print(format2, "981.30210E-8")

print()
# Check value from UNESCO 1983, p. 20
print("Checking sigma")
print()
print("S = 40, T = 40°C, P = 10000 dbar")
print(format1 % "sigma(40, 40, 10000)", sigma(40, 40, 10000))
print(format2, 59.82037)

print()
# Check value from UNESCO 1983, p. 11
print("Checking salt")
print()
print("Salinity = 40.0000")
print("cond = 1.888091, T = 40°C, P = 10000 dbar")
print(format1 % "salt(1.888091, 40, 10000)", salt(1.888091, 40, 10000))
print(format2, 40.0000)

print()
# Check value from UNESCO 1983, p. 11
print("Checking cond")
print()
print("S = 40, T = 40°C, P = 10000 dbar")
print(format1 % "cond(40, 40, 10000)", cond(40, 40, 10000))
print(format2, 1.888091)

print()
# Check value from UNESCO 1983, p. 35
print("Checking heatcap")
print()
print("S = 40, T = 40°C, P = 10000 dbar")
print(format1 % "heatcap(40, 40, 10000)", heatcap(40, 40, 10000))
print(format2, "3849.500")

print()
# Check value from UNESCO 1983, p. 36
print("Checking adtgrad")
print()
print("S = 40, T = 40°C, P = 10000 dbar")
print(format1 % "adtgrad(40, 40, 10000)", adtgrad(40, 40, 10000))
print(format2, "3.255976E-4")

print()
# Check value from UNESCO 1983, p. 44
print("Checking temppot")
print()
print("S = 40, T = 40°C, P = 10000 dbar, Pref = 0")
print(format1 % "temppot(40, 40, 10000)", temppot(40, 40, 10000))
print(format2, 36.89073)

print()
# Check value from UNESCO 1983, p. 30
print("Checking freezept")
print()
print("S = 40, p = 500 dbar")
print(format1 % "freezept(40, 500)", freezept(40, 500))
print(format2, -2.588567)

print()
# Check value from UNESCO 1983, p. 49
print("Checking soundvel")
print()
print("S = 40, T = 40°C,  P = 10000 dbar")
print(format1 % "soundvel(40, 40, 10000)", soundvel(40, 40, 10000))
print(format2, 1731.995)

print()
# Check value from UNESCO 1983, p. 28
print("Checking depth")
print()
print("P = 10000 dbar, latitude = 30 degrees")
print(format1 % "depth(10000, 30)", depth(10000, 30))
print(format2, 9712.653)
