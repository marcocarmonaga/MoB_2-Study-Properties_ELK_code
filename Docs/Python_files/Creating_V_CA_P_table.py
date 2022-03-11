# Importando módulos

import numpy as np
from typing import List

# Definiendo constantes

V0: float = 178.3437592
B0: float = 0.1024416633E-01  # Ha/Bohr^3
B_PRIME: float = 4.190756356
C0_A0: float = 1.0958578897109787

# Definiendo conjunto de datos

DATA = np.loadtxt('/home/marcocarmonaga/Documents/Elk_projects/MoB_2_project/c_a_vs_Energy/fits/v_vs_c_a_vs_energy.txt')

PRESSURES: List[float] = []  # GPa
VOLUMES: List[float] = DATA[:,0]
C_A_VALUES: List[float] = DATA[:,1]

# Definiendo funciones auxiliares


def P(V: float) -> float:
    return (3 / 2) * GPa(B0) * ((V0 / V)**(7/3) - (V0 / V)**(5/3)) * (1 + (3/4)*(B_PRIME - 4)*((V0 / V)**(2 / 3) - 1))  # GPa


def GPa(Ha_Bohr_3: float) -> float:
    return Ha_Bohr_3 * 29421.02648438959  # GPa

def GETTING_PRESSURES():
    for volume in VOLUMES:
        pressure = P(volume)
        PRESSURES.append(pressure)
        
def SAVING():
    file = open(
        '/home/marcocarmonaga/Documents/Elk_projects/MoB_2_project/c_a_vs_Energy/fits/V_CA_P.txt', 'w')
    for pressure, volume, c_a_value in zip(PRESSURES, VOLUMES, C_A_VALUES):
        file.write(f'{volume} {c_a_value} {pressure}\n')
    file.close()
    
def main():
    GETTING_PRESSURES()
    SAVING()
    
if __name__ == '__main__':
    main()