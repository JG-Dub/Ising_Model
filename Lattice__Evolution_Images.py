#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import Ising_Functions as I
import matplotlib.pyplot as plt

#Displays lattice evolution as images
kt = 4
h = 0
J = 1
Lat = I._init_lattice(50,0)
plt.figure(1)
plt.imshow(Lat, interpolation = 'none')
Lat, s, M_a, E_a, M_asq, E_asq, M_sq, E_sq, M, E, lis_i   = I.newlattice(Lat,10000,kt,J,0)
plt.figure(2)
plt.imshow(Lat, interpolation = 'none')
Lat, s, M_a, E_a, M_asq, E_asq, M_sq, E_sq, M, E, lis_i   = I.newlattice(Lat,100000,kt,J,0)
plt.figure(3)
plt.imshow(Lat, interpolation = 'none')
Lat, s, M_a, E_a, M_asq, E_asq, M_sq, E_sq, M, E, lis_i   = I.newlattice(Lat,200000,kt,J,0)
plt.figure(4)
plt.imshow(Lat, interpolation = 'none')



