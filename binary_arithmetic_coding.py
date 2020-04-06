#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 16:32:59 2019

@author: samruddhi
"""
import numpy as np

def Arithmetic_Coding(I):
    
    Seq = ''
    dc = I[0]
    # Removing the trailing zeros:-
    nz_ind = np.nonzero(I)
    x = np.shape(nz_ind)[1]
    #Ig = I[1:(x + 1)]
    
    k = 1
    while k <= len(I):
        if k >= (x + 1):
            # Code 1:
            #Seq.append('1')
            Seq += '1'
            break
        else:
            # Code 0:
            #Seq.append('0')
            Seq += '0'
            
            V = I[k]
            while V == 0:
                # Code 0:
                #Seq.append('0')
                Seq += '0'
                k += 1
                V = I[k]
                
            # Code 1:
            #Seq.append('1')
            Seq += '1'
            
            # Encode V:
            if V < 0:
                #Seq.append('1')
                Seq += '1'
            else:
                #Seq.append('0')
                Seq += '0'
            
            Sz = np.abs(V) - 1
            n1 = np.floor(np.log2(Sz))
            n1 = n1.astype(int)
            for i in range(n1+2):
                #Seq.append('1')
                Seq += '1'
            
            #Seq.append('0')
            Seq += '0'
            
            if n1 > 0:
                Szr = Sz - (2**n1)
                Seq += np.binary_repr(Szr, n1)
        k += 1
    
    return Seq, dc
