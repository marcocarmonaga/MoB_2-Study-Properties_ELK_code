# Importing modules
from audioop import lin2adpcm
import math as m
import os
import webbrowser

# Defining variables / list
c_a_values = [0.986, 1.008, 1.030, 1.052, 1.074, 1.096, 1.118, 1.140, 1.162, 1.183, 1.206]

# Volume (change it)
V = 194.7

a_values = [((2 * V) / (m.sqrt(3) * c_a_value))**(1/3) for c_a_value in c_a_values]
a_values = [round(a_value, 5) for a_value in a_values]

x = range(1,12,1)

dirs = [os.mkdir(f'./{c_a_value}') for c_a_value in c_a_values]

paths = [f'./{c_a_value}' for c_a_value in c_a_values]

# Defining text
s = " "

l1 = "!MoB2_hex_gga_nk18_rkmax7.0_gmax12.0_w0.20"

l2 = "tasks"
l3 = "  0"

l4 = "! lattice vector optimisation while maintaining the unit cell volume"
l5 = "!latvopt"
l6 = "!  2"

l7 = "! high-quality calculation for precise total energies"
l8 = "highq"
l9 = " .true."

l10 = "! switch off automatic determination of the k-point grid"
l11 = "autokpt"
l12 = " .false."

l13 = "ngridk"
l14 = "  18 18 18"

l15 = "! shift of k-point offset"
l16 = "vkloff"
l17 = "  0.0  0.0  0.5"

l18 = "! type of smearing 0-->Gaussian 3--> Fermi-Dirac(default)"
l19 = "!stype"
l20 = "!  0"

l21 = "! value of the smearing (Ry)"
l22 = "!swidth"
l23 = "!  0.20"

l24 = "! default value is 7.0"
l25 = "!rgkmax"
l26 = "!  7.0"

l27 = "! default value is 12.0"
l28 = "!gmaxvr"
l29 = "!  12.0"

l30 = "! PBE exchange-correlation functional"
l31 = "xctype"
l32 = "  20"

l33 = "! speed the calculation up with Broyden mixing"
l34 = "mixtype"
l35 = "  3"

l36 = "! lattice vectors of the crystal"
l37 = "avec"
l38 = "  .8660254037844386 -0.5  0.0  "
l39 = "  0.0    1.0  0.0 "
ls40 = [f'  0.0    0.0  {c_a_value}' for c_a_value in c_a_values]

l41 = "scale"
ls42 = [f'  {a_value}' for a_value in a_values]

l43 = "sppath"
l44 = "  '/home/marcocarmonag/Documents/elk-7.2.42/species/'"

l45 = "atoms"
l46 = "  2                                    : nspecies"
l47 = "  'Mo.in'                              : spfname"
l48 = "  1                                    : natoms; atposl below"
l49 = "  0.0         0.0         0.0"
l50 = "  'B_RMTfix.in'"
l51 = "  2"
l52 = "  .6666666666666666  .3333333333333333  0.5"
l53 = "  .3333333333333333  .6666666666666666  0.5"

# Zipping
values = zip(x,dirs,paths, c_a_values, a_values, ls40, ls42)

# Creating the directories
for x_i, dir,path, c_a_value, a_value, l40 , l42 in values:
    with open(f'./{path}/elk.in', 'w') as file:
        file.writelines('{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(l1,s,l2,l3,s,l4,l5,l6,s,l7,l8,l9,s,l10,l11,l12,s,l13,l14,s,l15,l16,l17,s,l18,l19,l20,s,l21,l22,l23,s,l24,l25,l26,s,l27,l28,l29,s,l30,l31,l32,s,l33,l34,l35,s,l36,l37,l38,l39,l40,s,l41,l42,s,l43,l44,s,l45,l46,l47,l48,l49,l50,l51,l52,l53))
        file.close()