from matplotlib import markers
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

v_vs_c_a_vs_energy = np.loadtxt('/home/marco/Documents/Elk_projects/MoB_2_project/c_a_vs_Energy/fits/v_vs_c_a_vs_energy.txt')
v = v_vs_c_a_vs_energy[:,0]
c_a = v_vs_c_a_vs_energy[:,1]
energy = v_vs_c_a_vs_energy[:,2]

fig = plt.figure()
fig.set_size_inches(6, 6)
ax = fig.add_subplot(111, projection='3d')
ax.scatter(v,c_a,energy, color='r')
ax.set_title("V vs $c/a$ vs Energy")
ax.set_xlabel("V")
ax.set_ylabel("$c/a$")
ax.set_zlabel("Energy")
plt.show()