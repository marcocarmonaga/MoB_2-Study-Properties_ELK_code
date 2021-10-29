import numpy as np
import matplotlib.pyplot as plt

V0 = 178.3437592
B0 = 0.1024416633e-01
B0_prime = 4.190756356
c0_a0 = 1.0958578897109787

def P(V):
    return (3 * B0 / 2) * ((V0 / V)**(7 / 3)-(V0 / V)**(5 / 3))*(1+(3 / 4)*(B0_prime - 4)*((V0 / V)**(2 / 3) - 1))

def beta(c_a,V,alpha):
    return ((((c_a)-(c0_a0))/(1-(V / V0)))-alpha)/(1-(V / V0))

df = np.loadtxt('/home/marco/Documents/Elk_projects/MoB_2_project/c_a_vs_Energy/fits/v_vs_c_a_vs_energy.txt')

print(df)