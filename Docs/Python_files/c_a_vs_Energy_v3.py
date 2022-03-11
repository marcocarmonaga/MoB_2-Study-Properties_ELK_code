from cProfile import label
from turtle import color
from importlib_metadata import files
from isort import file
import numpy as np
import matplotlib.pyplot as plt
import os

poly_coefficients_set = np.loadtxt('/home/marco/Documents/Elk_projects/MoB_2_project/c_a_vs_Energy/fits/poly_coefficients.txt')

poly_coefficients = [poly_coefficients_set[i,:] for i in range(0,11,1)]

files = os.listdir('/home/marco/Documents/Elk_projects/MoB_2_project/c_a_vs_Energy/data/')

for poly_coefficient, file in zip(poly_coefficients, files):
    df = np.loadtxt(f'{file}')
    x = df[:,0]
    y = df[:,1]
    p = np.poly1d(poly_coefficient)
    z = np.linspace(0.986,1.206,100)
    fig, ax = plt.subplots()
    ax.plot(z, p(z), color='r', label = '4th-grade polynomial curve fitting')
    ax.scatter(x,y)
    plt.title('$c/a$ vs Energy')
    plt.xlabel('$c/a$')
    plt.ylabel('Energy')
    plt.legend()
    fig.savefig(f'/home/marco/Documents/Elk_projects/MoB_2_project/c_a_vs_Energy/plots/{file}.png')