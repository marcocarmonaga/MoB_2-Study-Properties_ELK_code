from math import *
import os
import numpy as np

files = [0,50,65,70,80,90,100,110,120,130,140,150]

data = np.loadtxt(
    '/home/marcocarmonaga/Documents/Elk_projects/MoB_2_project/c_a_vs_Energy/fits/P_V_c_a_copy.txt')

# CONSTANTES
spec = '/home/marcocarmonaga/Elk/elk-7.2.42/species/'
k = 18
rkm = 8
gm = 16
wid = 0.20
hh = 0.5*sqrt(3)
to1 = 1.0/3.0
to2 = 2.0/3.0

# VARIABLES
vo0_s = data[:, 1]
ca_s = data[:, 2]
aa_s = [exp(log(vo0/(ca*hh))/3) for vo0, ca in zip(vo0_s, ca_s)]

elk_files = [[f'!NbMoB2_x100_hex_gga_nk{k}_rkmax{rkm}_gmax{gm}_w{wid}\n', '\n', 'tasks\n', '  0\n', '  10\n', '  20\n', '\n', '! lattice vector optimisation while maintaining the unit cell volume\n', '!latvopt\n', '!  2\n', '\n', '! high-quality calculation for precise total energies\n', 'highq\n', ' .true.\n', '\n', '! switch off automatic determination of the k-point grid\n', 'autokpt\n', ' .false.\n', '\n', 'ngridk\n', f'  {k} {k} {k}\n', '\n', '! shift of k-point offset\n', 'vkloff\n', '  0.0  0.0  0.5\n', '\n', '! type of smearing 0-->Gaussian 3--> Fermi-Dirac(default)\n', '!stype\n', '!  0\n', '\n', '! value of the smearing (Ry)\n', '!swidth\n', f'!  {wid}\n', '\n', '! default value is 7.0\n', 'rgkmax\n', f'  {rkm}\n', '\n', '! default value is 12.0\n', 'gmaxvr\n', f'  {gm}\n', '\n', '! PBE exchange-correlation functional\n', 'xctype\n', '  20\n', '\n', '! speed the calculation up with Broyden mixing\n', 'mixtype\n', '  3\n', '\n', '! lattice vectors of the crystal\n','avec\n', f'  {hh} -0.5  0.0\n', f'  0.0    1.0  0.0\n', f'  0.0    0.0  {ca}\n', '\n', 'scale\n', f'  {aa}\n', '\n', '! These are the vertices to be joined for the band structure plot\n', 'plot1d\n', '  8 400                      : nvp1d, npp1d\n', '  0.00   0.00   0.00  !G       : vlvp1d\n', '  0.00   0.50   0.00  !M\n', f'  {to1} {to1} 0.00  !K\n', '  0.00   0.00   0.00  !G\n', '  0.00   0.00   0.50  !A\n', '  0.00   0.50   0.50  !L\n', f'  {to1} {to1} 0.50  !H\n', '  0.00   0.00   0.50  !A\n', '\n', '! details for DOS calcs\n', 'wplot\n', '800\n', '1000\n', '1\n', '-0.8 0.5\n', '\n', 'sppath\n', f"  '{spec}'\n", '\n', 'atoms\n', '  2                                    : nspecies\n', "  'Mo.in'                              : spfname\n", '  1                                    : natoms; atposl below\n', '  0.0         0.0         0.0\n', "  'B_RMTfix.in'\n", '  2\n', f'  {to2}  {to1}  0.5\n', f'  {to1}  {to2}  0.5\n'] for vo0, ca, aa in zip(vo0_s, ca_s, aa_s)]

def CREATING():
    for file in files:
        os.mkdir(f'/home/marcocarmonaga/Documents/Elk_projects/MoB_2_project/c_a_vs_Energy/bandas/{file}')
    
def CREATING2():
    for elk_file,file in zip(elk_files,files):
        with open(f'/home/marcocarmonaga/Documents/Elk_projects/MoB_2_project/c_a_vs_Energy/bandas/{file}/elk.in','a') as elk:
            elk.writelines(elk_file)
            elk.close()

def main():
    CREATING()
    CREATING2()

if __name__ == '__main__':
    main()