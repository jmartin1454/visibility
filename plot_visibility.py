#!/usr/bin/python3

# Makes Fig. 1 and Fig. 2

# from C. ABEL et al. PHYSICAL REVIEW A 99, 042112 (2019)

from visibility import *

import matplotlib.pyplot as plt
import numpy as np

g10=np.arange(-30,30,0.01) # pT/cm
alpha=alpha_rev(g10*1e-12*1e+2)
plt.plot(g10,alpha,label='Eq. (22) -- reversible Ramsey wrapping')
plt.title('UCN polarization after T = 180 s storage')
plt.xlim(-60,60)
plt.ylim(0.6,0.91)
plt.xlabel(r'$G_{1,0}$ (pT/cm)')
plt.ylabel(r'$\alpha$')
# add a plot of the irreversible T2 from Fig. 2
g10=np.arange(-60,60,0.01) # pT/cm
alpha=alpha_irrev(0,0,g10*1e-12*1e+2)
plt.plot(g10,alpha,label='Eq. (29) -- irreversible/intrinsic T2')
plt.legend()
plt.show()

g1p1=np.arange(-300,300,0.01) # pT/cm
alpha=alpha_irrev(g1p1*1e-12*1e+2,0,0)
plt.plot(g1p1,alpha)
plt.title('UCN polarization after T = 180 s storage')
plt.xlim(-300,300)
plt.ylim(0.,0.84)
plt.xlabel(r'$G_{1,1}$ (pT/cm)')
plt.ylabel(r'$\alpha$')
plt.show()
