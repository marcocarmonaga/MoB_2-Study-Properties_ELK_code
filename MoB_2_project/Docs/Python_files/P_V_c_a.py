import numpy as np

V_0 = 178.3437592
c0_a0 = 1.0958578897109787
B_0                =           0.1024416633E-01
B_prime               =            4.190756356 

df = np.loadtxt('/home/marcocarmonaga/Documents/Elk_projects/MoB_2_project/c_a_vs_Energy/fits/v_vs_c_a_vs_energy.txt')

V = df[:,0]

C_A = df[:,1]

def P(V):
    return (3 * B_0 / 2)*((V_0/V)**(7/3)-(V_0/V)**(5/3))*(1+(3/4)*(B_prime-4)*((V_0/V)**(2/3)-1))

for v, c_a in zip(V,C_A):
    print(np.array((P(v), v, c_a)))