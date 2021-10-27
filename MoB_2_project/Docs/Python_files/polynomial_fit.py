import os
import numpy as np
from numpy.lib.polynomial import roots
import cmath

files = os.listdir()

for file in files:
    data = np.loadtxt(f'{file}')
    x = data[:,0]
    y = data[:,1]
    coef_p = np.polyfit(x , y, 4)
    der_p = np.array([coef_p[0]*4 , coef_p[1]*3 , coef_p[2]*2 , coef_p[3]])
    roots = np.roots(der_p)
    p = np.poly1d(coef_p)
    for root in roots:
        if root.imag == 0:
            print(f'{file} {root} {p(root)}')