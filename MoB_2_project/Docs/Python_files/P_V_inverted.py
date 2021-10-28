import numpy as np
import matplotlib.pyplot as plt

V0 = 178.3437592
E0 = -4099.369449
B0 = 0.1024416633e-01
B0_prime = 4.190756356


def P(V):
    return (3 * B0 / 2) * ((V0 / V)**(7 / 3)-(V0 / V)**(5 / 3))*(1+(3 / 4)*(B0_prime - 4)*((V0 / V)**(2 / 3) - 1))

def c_a(V):
    return (c / a) * (V0) + alpha(1-V/V0) +beta(1-V/V0)^2,


volumes = [159.30, 194.70, V0, 162.84, 169.92, 184.08,
           177.00, 173.46, 180.54, 191.16, 187.62, 166.38]

pressure_points = [P(volume) for volume in volumes]

for volume, pressure_point in zip(volumes, pressure_points):
    print(volume, pressure_point)
