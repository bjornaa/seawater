#! /usr/bin/env python
# --- encoding: iso-8859-1 ---


# Python test script for the density functions in the seawater module
#
# 15 October 2000
#
# Bj�rn �dlandsvik (bjorn@imr.no)
# Institute of Marine Research
# P.O.Box 1870 Nordnes
# N-5817 Bergen, NORWAY

# This script tries to recreate the density tables from pp 22-24
# in the UNESCO 1983 report. The functions tested are dens, svan
# and sigma.

# Reference:
# UNESCO 1983
# N.P. Fofonoff and R.C. Millard Jr.,
# Algorithms for computation of fundamental properties of seawater,
# Unesco technical papers in marine science 44.

from seawater import dens, svan, sigma
from Numeric import array, arange

# Declare argument arrays
S = array([0., 30., 35., 40.])
T = 10.0*arange(5)
P = 1000.0*arange(11)

deg = chr(176)  # degree symbol in iso-latin1 encoding

# ----------------------------------------------------------

def printsvan():
    entry = "     %7.2f"
    print # empty line
    print "                SPECIFIC VOLUME ANOMALY DELTA [1.0e-8 M**3/KG]"
    print "PRESSURE                     TEMPERATURE",
    print deg+"C  IPTS-68                 SALINTY:", "%2.0f" % S[0]
    print "DECIBARS %8d %11d %11d %11d %11d" % tuple(T)
    for p in P:
        print "%6.0f" % p, 5*entry % tuple(1.0e8*svan(S[0],T,p))
    for s in S[1:]:
        print 68*"-" + "SALINTIY:", "%2.0f" % s
        for p in P:
            print "%6.0f" % p, 5*entry % tuple(1.0e8*svan(s,T,p))

# ------------------------------------------------------
                                         
def printsigma():
    entry = "     %7.4f"
    print # empty line
    print "                          DENSITY ANOMALY SIGMA [KG/M**3]"
    print "PRESSURE                     TEMPERATURE",
    print deg+"C  IPTS-68                 SALINTY:", "%2.0f" % S[0]
    print "DECIBARS %8d %11d %11d %11d %11d" % tuple(T)
    for p in P:
        print "%6.0f" % p, 5*entry % tuple(sigma(S[0],T,p))
    for s in S[1:]:
        print 68*"-" + "SALINTIY:", "%2.0f" % s
        for p in P:
            print "%6.0f" % p, 5*entry % tuple(sigma(s,T,p))

# --------------------------------------------------------

def printvol():
    entry = "   %9.7f"
    print # empty line
    print "                         SPECIFIC VOLUME V [1e-3 M**3/KG]"
    print "PRESSURE                     TEMPERATURE",
    print deg+"C  IPTS-68                 SALINTY:", "%2.0f" % S[0]
    print "DECIBARS %8d %11d %11d %11d %11d" % tuple(T)
    for p in P:
        print "%6.0f" % p, 5*entry % tuple(1e3 / dens(S[0],T,p))
    for s in S[1:]:
        print 68*"-" + "SALINTIY:", "%2.0f" % s
        for p in P:
            print "%6.0f" % p, 5*entry % tuple(1e3 / dens(s,T,p))

#################################################

printsvan()
raw_input("press any key to continue")
printsigma()
raw_input("press any key to continue")
printvol()
