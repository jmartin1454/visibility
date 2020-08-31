# implements equations (22) and (29)

# from C. ABEL et al. PHYSICAL REVIEW A 99, 042112 (2019)

from math import *
import numpy as np
from scipy.constants import physical_constants as pc
from scipy.constants import find

gamma_n=pc["neutron gyromag. ratio"][0]  # rad/s/T

#gamma_n=2*pi*30.*1e6 # rad/s/T, neutron gyromagnetic ratio

# Equation (22) is integrated at the bottom of page 6 (after Fig. 1 is
# first mentioned) to give this equation

def alpha_rev(g10):
    alpha_0=0.76 # dimensionless
    varzbar=0.18 # cm^2, variance of neutron z distribution
    varzbar=varzbar*0.01**2 # m^2, variance of neutron z distribution
    T=180 # s, neutron free-precession time
    return alpha_0-0.5*gamma_n**2*g10**2*varzbar*T**2

# Equation (29) is employed in Equation (31); both are implemented

def T2mag(g1p1,g1m1,g10):
    R=.47/2 # m, radius of chamber
    v=3 # m/s, neutron speed
    H=.12 # m, height of chamber
    T2mag_inverse=8*R**3*gamma_n**2/(9*pi*v)*(g1p1**2+g1m1**2)+H**3*gamma_n**2/(16*v)*g10**2
    return 1/T2mag_inverse

def alpha_irrev(g1p1,g1m1,g10):
    alpha_0=0.75 # dimensionless
    T=180 # s, neutron free-precession time
    return alpha_0*np.exp(-T/T2mag(g1p1,g1m1,g10))
