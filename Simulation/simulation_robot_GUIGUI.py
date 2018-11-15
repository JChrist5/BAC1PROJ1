"""
Programme réalisé par Guillaume VDREST et  Théo VDD
Novembre 2018
"""

import math
import matplotlib.pyplot as plt
import numpy as np


l1 = 30
l2 = 30
h2 = 10
l3 = 30
l4 = 7
h4 = 5
Elastic = 15
Volant = 20
Pot = 25
Poids_voiture = 4*9.806
Frot_mu = 0.6
travail_Frot = 0

global step

step = 0.1    # pas de simulation [m]
end = l1+l2+l3+l4       # fin de la simulation [m]

def direction(l):
    """
    pre: l distance parcourue [m]
    post: retourne la direction du robot à la distance l [rad]
    """
    if 0<=l<=l1:
        return 0
    if l1<l<=l1+l2:
        a = -h2*math.sin(((math.pi*2)*l/l2)-l1)/2
        b = -h2*math.sin(((math.pi*2)*(l+step)/l2)-l1)/2
        return (b-a)
    if l1+l2<l<=l1+l2+l3:
        return 0
    if l1+l2+l3<l<=l1+l2+l3+l4:
        return (h4/l4)*step


def y_pos_array(x_lst):
    """
    Determine the y position of the car
    """
    y = np.empty(len(x_lst))
    y[0] = 0
    for i in range(len(y)+1):
        try:
            y[i] = y[i-1] + direction(x_lst[i])
        except:
            pass
    return y


def compute_distance(x_lst,y_lst):
    """
    Compute the distance done in a certain interval dy/dx.
    Return an np array of the dl (related to dx)
    """
    distance = np.empty(len(x_lst))
    for i in range(len(x_lst)):
        try:
            distance[i] = ((y_lst[i+1]-y_lst[i])**2 + (x_lst[i+1]-x_lst[i])**2)**0.5
        except:
            pass
    return distance


def compute_inclinaison(x_lst, y_lst):
    """
    Compute the inclinaison on dy/dx
    Return an np array of the angle (related to dx)
    """
    inclinaison = np.empty(len(x_lst))
    for i in range(len(x_lst)):
        try:
            inclinaison[i] = math.atan((y_lst[i+1]-y_lst[i])/(x_lst[i+1]-x_lst[i]))
        except:
            pass
    return inclinaison


def compute_kinetic_energy(x_lst):
    kinetic_energy = np.empty(len(x_lst))
    return


def compute_potential_energy(x_lst,y_lst):
    """
    Compute the potential energy of the car
    Return an np array of the potential energy (in Joules)
    """        
    potential_energy = np.empty(len(x_lst))
    for i in len(x_lst):
        potential_energy[i] = y_lst[i] * Poids_voiture        
    return potential_energy


def internal_friction_work(distance_list, equ_friction_coef):
    """
    Compute the work done by internal friction during a certain distance.
    Return an np array of the work done in a certain interval of distance dl
    """
    friction_work = np.empty(len(distance_lst))
    for i in range(len(distance_lst)):
        try:
            friction_work[i] = -1 * distance_lst[i] * equ_friction_coef 
        except:
            pass
    return friction_work


def compute_friction_work(distance_lst, inclinaison, friction_coef, car_weight):
    """
    Compute the work done by friction during a certain distance. Take care of the inclinaison
    Return an np array of the work done in a certain interval of distance dl
    """
    friction_work = np.empty(len(distance_lst))
    for i in range(len(distance_lst)):
        try:
            friction_work[i] = -1 *distance_lst[i] * math.cos(inclinaison[i]) * friction_coef * car_weight 
        except:
            pass
    return friction_work


def compute_total_work(f_work_lst):
    total_work = np.empty(len(f_work_lst))
    total_work[0] = 100
    for i in range(len(f_work_lst)):
        try:
            total_work[i+1] = total_work[i] + f_work_lst[i]
        except:
            pass
    return total_work 




"""
x = np.arange(0, end, step)    # distance parcourue [m]
y = y_pos_array(x)
distance = compute_distance(x,y)
inclinaison = compute_inclinaison(x,y)
f_work = compute_friction_work(distance,inclinaison,Frot_mu,Poids_voiture)
e_tot = compute_total_work(f_work)

l = np.arange(0,end, step)
x = np.empty(len(l))       # position x [m]
y = np.empty(len(l))
Erg = np.empty(len(l))       # position y [m]
Ecin = np.empty(len(l))
Frottements = np.empty(len(l))

Distance = np.empty(len(l))
Frau_angle = np.empty(len(l))
travail_Frot = np.empty(len(l))

y[0] = 0
Erg[0] = Elastic + Volant + Pot



for i in range(len(l)-1):
    # simulation du pas i+1
    dl = step
    d = direction(l[i])
    x[i+1] = x[i] + dl
    y[i+1] = y[i] + d
    Distance[i] = ((y[i+1]-y[i])**2 + (x[i+1]-x[i])**2)**0.5 #Calcule dl pour chaque dy/dx
    Frau_angle[i] = math.atan((y[i+1]-y[i])/(x[i+1]-x[i])) #Calcule l'angle d'inclinaison du véhicule pour chaque dy/dx
    travail_Frot[i] = Distance[i] * Frot_mu * Poids_voiture * math.cos(Frau_angle[i]) #Calcule le travail de frottement pour chaque dl
    Erg[i+1] = Erg[i] - travail_Frot[i]


plt.subplot(221, aspect='equal')  # grille 2x1, 2e graphique
plt.plot(x, y, 'red', label="trajectoire")

plt.subplot(222, aspect='equal')  # grille 2x1, 2e graphique
plt.plot(x, travail_Frot, 'red', label="distance")

plt.subplot(223, aspect='equal')  # grille 2x1, 2e graphique
plt.plot(x, Erg, 'red', label="distance")
"""

x = np.arange(0, end, step)    # distance parcourue [m]
y = y_pos_array(x)
distance = compute_distance(x,y)
inclinaison = compute_inclinaison(x,y)
f_work = compute_friction_work(distance,inclinaison,Frot_mu,Poids_voiture)
e_tot = compute_total_work(f_work)

plt.subplot(221, aspect='equal')  # grille 2x1, 2e graphique
plt.plot(x, y, 'red', label="trajectoire")

plt.subplot(222, aspect='equal')  # grille 2x1, 2e graphique
plt.plot(x, f_work, 'blue', label="distance")

plt.subplot(223, aspect='equal')  # grille 2x1, 2e graphique
plt.plot(x, e_tot, 'blue', label="inclinaison")

plt.subplot(224, aspect='equal')  # grille 2x1, 2e graphique
plt.plot(x, e_tot, 'red', label="friction")

plt.show()