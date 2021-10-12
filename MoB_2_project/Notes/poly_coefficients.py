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
    print(coef_p)