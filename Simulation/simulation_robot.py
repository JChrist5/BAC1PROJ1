#
# Simulation: trajectoire d'un robot.
#
# Charles Pecheur 2018
#

import math
import matplotlib.pyplot as plt
import numpy as np





def direction(l):
    """
    pre: l distance parcourue [m]
    post: retourne la direction du robot à la distance l [rad]
    """
    return (math.pi * math.sin(l) + math.log(l+1))

### Paramètres de simulation

step = 0.01     # pas de simulation [m]
end = 20.0       # fin de la simulation [m]

### Variables de simulation

# chaque variable x est un tableau de valeurs x[i]
# pour chaque pas de simulation i

l = np.arange(0, end, step)    # distance parcourue [m]
x = np.empty(len(l))       # position x [m]
y = np.empty(len(l))       # position y [m]

### simulation

# conditions initiales
x[0] = 0
y[0] = 0

for i in range(len(l)-1):
    # simulation du pas i+1
    dl = l[i+1] - l[i]   
    d = direction(l[i])
    x[i+1] = x[i] + dl * math.cos(d)
    y[i+1] = y[i] + dl * math.sin(d)

### graphiques

plt.subplot(411)   # grille 4x1, 1er graphique
plt.plot(l, [direction(l1) for l1 in l])
plt.xlabel("l")
plt.ylabel("direction")

plt.subplot(412)   # grille 4x1, 2e graphique
plt.plot(l, x, label="x")
plt.plot(l, y, label="y")
plt.legend()

plt.subplot(212, aspect='equal')  # grille 2x1, 2e graphique
plt.plot(x, y, 'red', label="trajectoire")
plt.xlabel("x")
plt.ylabel("y")

plt.show()
