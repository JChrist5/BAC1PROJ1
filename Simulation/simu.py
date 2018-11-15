
import math
import matplotlib.pyplot as plt
import numpy as np
a = 10
b= 0

m=10
g=9.81

h = 7

steps = 0.1


end = a+b

all_steps = int(end/steps)

x = np.arange(0,end,steps)
y = np.empty(int(end/steps))

for i in range(int(end/steps)+1):
    try:
        y[i] = steps*np.sin(np.pi*(i/all_steps)) * h * 10
    except:
        pass



plt.subplot(411)   # grille 4x1, 1er graphique
plt.plot(x,y)

plt.subplot(412)
plt.plot(x,y*m*g)
plt.show()