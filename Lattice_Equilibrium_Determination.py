#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import Ising_Functions as I

#Evolution of energy and magnetisation as a function of iteration number

kt = 1
J = 1
h = 0
for i in range (1,2):
    
    Lat = I._init_lattice(20,1)
    Lattice, M_a, E_a, C_v, Magsep, M, E, lis_i  = I.newlattice(Lat,50000,kt,J,0)
    plt.figure(1)
    plt.plot(lis_i,E)
    plt.title("Energy Evolution")
    plt.xlabel('Iterations')
    plt.ylabel('Energy')
    
    plt.figure(2)
    plt.plot(lis_i,M)
    plt.title("Magnetization Evolution")
    plt.xlabel('Iterations')
    plt.ylabel('Magnetization')

    
plt.show()
