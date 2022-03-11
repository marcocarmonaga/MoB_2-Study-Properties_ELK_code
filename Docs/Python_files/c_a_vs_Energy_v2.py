import numpy as np
import matplotlib.pyplot as plt
import os

actual_dir = os.getcwd()
data_files = os.listdir(actual_dir)

print(data_files)

for data_file in data_files:
    df = np.loadtxt(f'{data_file}')
    energy = df[:,1]
    c_a = df[:,0]

    fig, ax = plt.subplots()
    ax.scatter(c_a, energy)

    ax.set(xlabel='c/a Value', ylabel='Energy', title='c/a vs Energy')
    ax.grid()

    fig.savefig(f'/home/marco/Documents/Elk_projects/MoB_2_project/c_a_vs_Energy/plots/{data_file}.png')