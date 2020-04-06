#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 15:24:30 2019

@author: samruddhi
"""
import os
import numpy as np
rng = 128

def sgn(X):
    Y = X / np.absolute(X)
    return Y

def jpegcos(k, l, A):
    if k == 0:
        return 1 / np.sqrt(A)
    else:
        return np.sqrt(2 / A) * np.cos((l + 0.5) * k * np.pi / A)
    


def max_stimuli(M, N):
    #range = 128
    coeff_max = np.zeros((M, N))
    xmax = np.zeros((M, N))
    
    for m in range(M):
        for n in range(N):
            for i in range(M):
                for j in range(N):
                    xmax[i, j] = rng * (1 + sgn(jpegcos(m, i, M) * jpegcos(n, j, N)))
                    coeff_max[m, n] += jpegcos(m, i, M) * jpegcos(n, j, N) * xmax[i, j]
                    
    return coeff_max

def quantization_matrix_adaptive(coeff_max, const):
    #range = 128
    M, N = np.shape(coeff_max)
    quant = np.zeros((M, N))
    Nn = np.sqrt(M*N)
    fmax = np.ceil(30 * np.sqrt((M-1)**2 + (N-1)**2) / (Nn * 1.5)) # Assuming pixel size is 1.5 min.
    for m in range(M):
        for n in range(N):
            f = 30 * np.sqrt(m**2 + n**2) / (Nn * 1.5)
            if f == 0:
                CSF = 1
            else:
                CSF = const * (f - fmax)
                # CSF = 100 * np.sqrt(f) * np.exp(-0.13*f)
            if m == 0 or n == 0:
                norm = 2**(-2.5)
                thresh = 1 / (norm*CSF)
            else:
                if m <= n:
                    OTF = np.exp(-9.5 * (m/n)**2)
                elif n < m:
                    OTF = np.exp(-9.5 * (m/n)**2)
                    
                if OTF < 0.5:
                    OTF = 0.5
                norm = 2**(-2)
                thresh = 1 / (norm*OTF*CSF)
                
            quant[m, n] = np.minimum(thresh * rng, coeff_max[m, n])
            
    return quant
            

def CSF_Quantization(bdct, const):
    m, n = np.shape(bdct)
    path = '/home/samruddhi/GSP_Compression/CSF_Quantization_Matrices_' + str(const)
    if not os.path.isdir(path):
        os.mkdir(path)
    
    try:
        quant = np.load(path + '/quant_' + str(m) + str(n) + '.npy')
    except FileNotFoundError:
        coeff_max = max_stimuli(m, n)
        quant = quantization_matrix_adaptive(coeff_max, const)
        np.save(path + '/quant_' + str(m) + str(n) + '.npy', quant)
    
    return np.around(bdct/quant)


    