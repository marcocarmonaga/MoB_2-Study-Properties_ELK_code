# Importando módulos

from typing import List
from sympy.solvers import solve
from sympy import Symbol
import cmath
import os

# Definiendo constantes

V0: complex = 178.3437592
B0: complex = 0.1024416633E-01  # Ha/Bohr^3
B_PRIME: complex = 4.190756356
C0_A0: complex = 1.0958578897109787
ALPHA: complex = -0.19145469
BETA: complex = 0.10026568

# Definiendo conjunto de datos

PRESSURES: List[complex] = [i for i in range(0, 151, 1)]  # GPa
VOLUMES: List[complex] = []
C_A_VALUES: List[complex] = []

# Definiendo funciones auxiliares


def P(V: complex) -> complex:
    return (3 / 2) * GPa(B0) * ((V0 / V)**(7/3) - (V0 / V)**(5/3)) * (1 + (3/4)*(B_PRIME - 4)*((V0 / V)**(2 / 3) - 1))  # GPa


def C_A(V: complex) -> complex:
    return C0_A0 + ALPHA*(1-(V / V0)) + BETA*((1-(V/V0))**2)


def GPa(Ha_Bohr_3: complex) -> complex:
    return Ha_Bohr_3 * 29421.02648438959  # GPa


def GETTING_VOLUMES():
    for pressure in PRESSURES:
        V = Symbol('V')
        volumes: List(complex) = solve(P(V) - pressure, 'V')
        VOLUMES.append(volumes[0])


def GETTING_C_A_VALUES():
    for volume in VOLUMES:
        c_a = C_A(volume)
        C_A_VALUES.append(c_a)


def SAVING():
    file = open(
        '/home/marcocarmonaga/Documents/Elk_projects/MoB_2_project/c_a_vs_Energy/fits/P_V_c_a.txt', 'w')
    for pressure, volume, c_a_value in zip(PRESSURES, VOLUMES, C_A_VALUES):
        file.write(f'{pressure} {volume} {c_a_value}\n')
    file.close()


def POWEROFF():
    os.system('shutdown now')
# Definiendo funcion principal


def main():
    GETTING_VOLUMES()
    GETTING_C_A_VALUES()
    SAVING()
    POWEROFF()

# Punto de inicio


if __name__ == "__main__":
    main()
