#!/usr/bin/python3

from math import *
from visibility import *

# This is an attempt to estimate some of our gradient goals

T2goal=10000 # s
print()
print('What is a reasonable T2?  Perhaps %f s?'%T2goal)
print()
T=180 # s
print('For a free-precession time of T=%f s'%T)
alpha=exp(-T/T2goal)
print('this sets an alpha goal of %f * alpha_0'%alpha)
print()
print('To achieve this alpha, we would need:')

# work out reversible alpha
alpha0=alpha_rev(0)
g10=0 # pT/cm
while(alpha_rev(g10*1e-12*1e+2)>alpha*alpha0):
   g10=g10+0.01
print('g10 < %f pT/cm'%g10)

# work out irreversible alpha
alpha0=alpha_irrev(0,0,0)
g1p1=0 # pT/cm
while(alpha_irrev(g1p1*1e-12*1e+2,0,0)>alpha*alpha0):
    g1p1=g1p1+0.01
print('sqrt(g1p1**2+g1m1**2) < %f pT/cm'%g1p1)
print()
