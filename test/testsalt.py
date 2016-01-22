#! /usr/bin/env python
# --- encoding: iso-8859-1 ---

# Python test script for the salinity functions in the seawater module
#
# 15 October 2000
#
# Bjørn Ådlandsvik (bjorn@imr.no)
# Institute of Marine Research
# P.O.Box 1870 Nordnes
# N-5817 Bergen, NORWAY

# This script tries to recreate the salinity tables from pp 13-14
# in the UNESCO 1983 report. The functions tested are salt and cond.

# Reference:
# UNESCO 1983
# N.P. Fofonoff and R.C. Millard Jr.,
# Algorithms for computation of fundamental properties of seawater,
# Unesco technical papers in marine science 44.

from seawater import salt, cond
from Numeric import array, arange

# Declare arrays

R = array([0.6990725, 0.9320967, 1.1651209, 1.3981451])
T = 10.0*arange(5)
P = 1000.0*arange(11)
S = array([25., 30., 35., 40.])

deg = chr(176)  # degree symbol in iso-latin1 encoding

# -----------------------------------------------------

def printsalt():
    entry = "     %7.4f"
    print # empty line
    print "                               SALINITY  S  [ PSS-78 ]"
    print "PRESSURE                     TEMPERATURE",
    print deg+"C  IPTS-68                COND. RATIO:"
    print "DECIBARS %8d %11d %11d %11d %11d" % tuple(T),
    print " %12.7f" % R[0]
    for p in P:
        print "%6.0f" % p,
        print 5*entry % tuple(salt(R[0],T,p))
    for r in R[1:]:
        print 68*"-" + "COND. RATIO:"
        print "%6.0f" % P[0],
        print 5*entry % tuple(salt(r,T,P[0])),
        print "%10.7f" % r
        for p in P[1:]:
            print "%6.0f" % p,
            print 5*entry % tuple(salt(r,T,p))


# ---------------------------------------------------------

# Conductiviy table p. 14

def printcond():
    entry = "    %8.6f"
    print #
    print "                              CONDUCTIVITY RATIO  R"
    print "PRESSURE                     TEMPERATURE",
    print deg +"C  IPTS-68                SALINITY:",
    print "%2.0f" % S[0]
    print "DECIBARS %8d %11d %11d %11d %11d"  % tuple(list(T))
    for p in P:
        print "%6.0f" % p,
        print 5*entry % tuple(cond(S[0],T,p))
    for s in S[1:]:
        print 68*"-" + "SALINITY:", "%2.0f" % s
        for p in P:
            print "%6.0f" % p,
            print 5*entry % tuple(cond(s,T,p))

# ------------------------------------------------------------

printsalt()
raw_input("press any key to continue:")
printcond()


