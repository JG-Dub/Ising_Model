#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import Ising_Functions as I
import matplotlib.pyplot as plt

# Plots lattice properties at various values of temperature
kt = 0.1
J = 1
n = 5
while kt<=5:
    Lat = I._init_lattice(n,0)
    C, M_a, E_a, C_v, Magsep, M, E, lis_i  = I.newlattice(Lat,50000,kt,J,0)
    plt.figure(1)
    plt.scatter(kt,E_a/(n*n))
    plt.xlabel('Temperature')
    plt.ylabel('Energy')
    plt.figure(2)
    plt.scatter(kt,abs(M_a/(n*n)))
    plt.xlabel('Temperature')
    plt.ylabel('Magnetization per spin')
    plt.figure(3)
    plt.scatter(kt,(1/kt**2)*(C_v/(n*n)))
    plt.xlabel('Temperature')
    plt.ylabel('C_v')
    plt.figure(4)
    plt.scatter(kt,(1/kt)*(Magsep/(n*n)))
    plt.xlabel('Temperature')
    plt.ylabel('Magnetic susceptibility')
    print (kt, M_a, E_a, C_v, Magsep)
    kt = kt + 0.1
plt.show()

    
