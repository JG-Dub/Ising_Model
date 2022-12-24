#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

#Create a random square matrix with values 1 and -1 
def _init_lattice(n,random):
    if random == 1:
        return np.random.choice([1, -1], size=(n,n))
    if random == 0:
        return np.random.choice([1, -1], size=(n,n))
    else:
        print('No configuration set')


#Function evaluates probability of transition
def prob_trans(E1,E2,kt):
    return np.exp((E1-E2)/kt)

#Moves arrays in x and y directions by +/- one position and multiplies this against the original lattice. This gives an array of energies at each site.
#Summing these results gives us the energy as per the hamiltonian
def energy(J,Lattice,h):
    return (-J*np.sum(Lattice*np.roll(Lattice, 1, axis = 0) + Lattice*np.roll(Lattice, -1, axis = 0) + Lattice*np.roll(Lattice, 1, axis = 1) + Lattice*np.roll( Lattice, -1, axis = 1)))/2 - np.sum(h*Lattice)

#Copies lattice and randomly selects 1 lattice site. Site is multiplied by -1 to flip spin
def newlattice(Lattice,interations,kt,J,h):
    lis_E = []
    lis_M = []
    lis_i = []
    E = 0
    s = 1
    M = 0
    Esq = 0
    Msq = 0
    for i in range (interations):
        new_Lattice = np.copy(Lattice)
        y = np.random.choice(Lattice.shape[0])
        x = np.random.choice(Lattice.shape[1])
        new_Lattice[y,x] = new_Lattice[y, x] * -1
        
    
        E1 = energy(J,Lattice,h)
        #print (E1)
        E2 = energy(J,new_Lattice,h)
        #print (E2)
    
        if E1 >= E2:
            Lattice = new_Lattice
            #print ('Flip accepted')
        else: 
            if prob_trans(E1,E2,kt) > np.random.random():
                Lattice = new_Lattice
                #print ('flip accepted with probability')
            
            else:
                Lattice = Lattice
                #print ('Flip not accepted')
        Mi = np.sum(Lattice)
        lis_E.append(energy(J,Lattice,h))
        lis_M.append(Mi)
        lis_i.append(i)
	# Allow for equilibration and sample every 1000 iterations
        if i > 10000 and i%1000==0:
            s = i - 10000
            E = E + energy(J,Lattice,h)
            M = M + np.sum(Lattice)
            Esq = Esq + energy(J,Lattice,h)**2
            Msq = Msq + np.sum(Lattice)**2
    #Calculating Observables
    #Average Energy
    E_a = E/s
    #Average Magnetisation
    M_a = M/s
    
    M = lis_M
    E = lis_E
    
    M_asq = M_a*M_a
    M_sq = Msq/(s)
    
    E_asq = E_a*E_a
    E_sq = Esq/(s)
    
    #Specfic Heat
    C_v = abs(E_sq - E_asq)
    
    #Magnetic Sucscepibility
    Magsep = abs(M_sq - M_asq)

        
    return Lattice, M_a, E_a, C_v, Magsep, M, E, lis_i








    






        
    



