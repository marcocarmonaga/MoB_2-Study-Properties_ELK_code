import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
df = np.loadtxt('./Energy_vs_c_a.txt')
energy = df[:,1]
c_a = df[:,0]

fig, ax = plt.subplots()
ax.plot(c_a, energy)

ax.set(xlabel='c/a Value', ylabel='Energy',
       title='Energy vs c/a at V = 177')
ax.grid()

fig.savefig("Energy_vs_c_a.png")
plt.show()
