#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 14:46:30 2019

@author: samruddhi
"""
import numpy as np

def hist_and_ind(CY):
    m, n = CY.shape[:2]
    # Creating the mean and variance matrices:-
    mn_mat = np.zeros((int(m/8), int(n/8)))
    var_mat = np.zeros((int(m/8), int(n/8)))
    b = np.zeros((8, 8))
    for k in range(int(m/8)):
        i = k*8
        for l in range(int(n/8)):
            j = l*8
            b = CY[i:i+8, j:j+8]
            #b = np.double(b)
            bshifted = b - 128
            mn_mat[k,l] = np.mean(bshifted)
            var_mat[k,l] = np.var(bshifted)
            
    #Tmn = np.std(mn_mat)
    #Tvar = np.std(var_mat)
    Tmn = np.std(np.std(mn_mat, axis=0))
    Tvar = np.std(np.std(var_mat, axis=0))

    #Forming a histogram based on mean and variance of each block:-
    s = 0
    Idx = np.zeros((int(m/8), int(n/8)))
    Idx = Idx.astype(int)
    Hist = []
    for i in range(int(m/8)):
        for j in range(int(n/8)):
            flag = 'n'
            if s > 0:
                #l = len(Hist)
                for k in range(s, 0, -1):
                    dv = np.absolute(var_mat[i,j] - Hist[k-1][2])
                    dm = np.absolute(mn_mat[i,j] - Hist[k-1][1])
                    if dv < Tvar and dm < Tmn:
                        Hist[k-1][3] += 1
                        Idx[i,j] = Hist[k-1][0]
                        flag = 'm'
                        break
            if flag == 'n':
                Hist.append([s, mn_mat[i,j], var_mat[i,j], 1])
                Idx[i,j] = s
                s += 1
    return Idx
