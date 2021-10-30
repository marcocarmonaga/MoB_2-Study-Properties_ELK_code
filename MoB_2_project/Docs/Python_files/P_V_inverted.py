import numpy as np

V0 = 178.3437592
c0_a0 = 1.0958578897109787

df = np.loadtxt('/home/marco/Documents/Elk_projects/MoB_2_project/c_a_vs_Energy/fits/v_vs_c_a_vs_energy.txt')

V = df[:,0]

C_A_C0_A0 = [c_a - c0_a0 for c_a in df[:,1]]

linear_coeffs = [1 - (v / V0) for v in V]
quadratic_coeffs =  [(1 - (v / V0))**2 for v in V]

A = [[linear_coeff, quadratic_coeff] for linear_coeff, quadratic_coeff in zip(linear_coeffs, quadratic_coeffs)]
A = np.array(A)

Q, R = np.linalg.qr(A)

b = np.vstack(C_A_C0_A0)

alpha, beta = np.linalg.solve(np.linalg.inv(R), Q.T.dot(b))

print(alpha, beta)
