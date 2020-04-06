#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 16:45:08 2019

@author: samruddhi
"""
import numpy as np
from scipy.fftpack import dct, idct
import pygsp as pygsp
#import matplotlib.pyplot as plt

def check(idx):
    #idx = idx.astype(np.int)
    idx1 = np.zeros_like(idx)
    #idx1 = idx1.astype(np.int)
    try:
        x = idx[0,0]
    except IndexError:
        x = idx[0]
    idx1 = idx - x
    if np.count_nonzero(idx1) == 0:
        return(True)
    else:
        return(False)

def dct2(a):
    return dct(dct(a.T, norm='ortho').T, norm='ortho')

def idct2(a):
    return idct(idct(a.T, norm='ortho').T, norm='ortho')

def zigzag(blk):
    M, N = np.shape(blk)
    Sdim = np.minimum(M, N)
    Ldim = np.maximum(M, N)
    SM = M + N - 2
    I = blk[0,0]
    for y in range(1, Sdim):
        idx = np.arange(y + 1)
        if y % 2 == 1: # y is odd
            I = np.hstack((I, blk[idx, y - idx]))
        else:
            I = np.hstack((I, blk[y - idx, idx]))
        
    if Sdim != Ldim:
        for y in range(Sdim, Ldim):
            if y % 2 == 0:  # y is even
                if M > N:
                    idx = np.arange(N)
                elif M < N:
                    idx = np.arange(y - M + 1, y + 1)
                I = np.hstack((I, blk[y - idx, idx]))
            else:
                if M > N:
                    idx = np.arange(y - N + 1, y + 1)
                elif M < N:
                    idx = np.arange(M)
                I = np.hstack((I, blk[idx, y - idx]))
                
    for y in range(Ldim, SM):
        if y % 2 == 0: # y is even
            idx = np.arange(y - M + 1, N)
            I = np.hstack((I, blk[y - idx, idx]))
            #if M > N:
            #    idx = np.arange(y - Ldim + 1, Sdim)
            #elif M < N:
            #    idx = np.arange(y - Sdim + 1, Ldim)
        else:
            idx = np.arange(y - N + 1, M)
            I = np.hstack((I, blk[idx, y - idx]))
            #if M > N:
            #    idx = np.arange(y - Sdim + 1, Ldim)
            #elif M < N:
            #    idx = np.arange((y - Ldim + 1, Sdim))
                
    I = np.hstack((I, blk[M - 1, N - 1]))
    return I

def gft2(blk):
    # Calculate the Weight Matrix W for each block:-
    W = calc_weight_mat(blk)
    G = pygsp.graphs.Graph(W)
    G.compute_fourier_basis()
    #bvec = blk
    bgft = G.gft(blk.flatten())
    return bgft, W

def sub2ind(arr_sh, m, n):
    M, N = arr_sh
    return N * m + n

def calc_weight_mat(blk):
    M, N = np.shape(blk)
    th = np.var(blk)
    W = np.zeros((M*N, M*N))
    offsets = np.array([[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]])
    
    for m in range(M):
        for n in range(N):
            idx = sub2ind([M, N], m, n)
            mN = m + offsets[:,0]
            nN = n + offsets[:,1]
            f = np.vstack((mN>=0, nN>=0, mN < M, nN < N))
            ixkeep = np.nonzero(np.all(f, axis=0))
            #ixkeep = np.nonzero((mN >= 0) and (nN >= 0) and (mN < M) and (nN < N))
            
            mt = mN[ixkeep]
            nt = nN[ixkeep]
            idx2 = sub2ind([M, N], mt, nt)
            
#            # Weighted graph:
#            alpha = 10
#            d = np.abs(blk[m, n] - blk[mt, nt])
#            W[idx, idx2] = 1/(1 + (d**2)/alpha)
#            W[idx2, idx] = W[idx, idx2]
            # Unweighted graph:
            tm = np.nonzero((blk[m, n] - blk[mt, nt]) < th)
            W[idx, idx2[tm]] = 1
            W[idx2[tm], idx] = 1
                    
    #W = 0
    return W

def igft2(coeffs, W):
    #m, n = sh
    #W = np.reshape(W_lin, (m*n, m*n))
    G = pygsp.graphs.Graph(W)
    G.compute_fourier_basis()
    brec = G.igft(coeffs)
    
    return brec
    
def calc_mse_psnr(A, B):
    mse = np.mean((A - B)**2)
    if mse == 0:
        psnr = 100
    else:
        PIXEL_MAX = 255.0
        psnr = 20 * np.log10(PIXEL_MAX / np.sqrt(mse))
    return mse, psnr

def zigzag_re(I, M, N):
    Sdim = np.minimum(M, N)
    Ldim = np.maximum(M, N)
    SM = M + N - 2
    blk = np.zeros((M, N))
    blk[0, 0] = I[0]
    k = 1
    for y in range(1, Sdim):
        idx = np.arange(y + 1)
        if y % 2 == 1: # y is odd
            blk[idx, y - idx] = I[k:k+y+1]
            k += y + 1
        else:
            blk[y - idx, idx] = I[k:k+y+1]
            k += y + 1
        
    if Sdim != Ldim:
        for y in range(Sdim, Ldim):
            if y % 2 == 0:  # y is even
                if M > N:
                    idx = np.arange(N)
                elif M < N:
                    idx = np.arange(y - M + 1, y + 1)
                blk[y - idx, idx] = I[k:k + idx.shape[0]]
                k += idx.shape[0]
                #I = np.hstack((I, blk[y - idx, idx]))
            else:
                if M > N:
                    idx = np.arange(y - N + 1, y + 1)
                elif M < N:
                    idx = np.arange(M)
                blk[idx, y - idx] = I[k:k + idx.shape[0]]
                k += idx.shape[0]
                #I = np.hstack((I, blk[idx, y - idx]))
                
    for y in range(Ldim, SM):
        if y % 2 == 0: # y is even
            idx = np.arange(y - M + 1, N)
            blk[y - idx, idx] = I[k:k + idx.shape[0]]
            k += idx.shape[0]
            #I = np.hstack((I, blk[y - idx, idx]))
            #if M > N:
            #    idx = np.arange(y - Ldim + 1, Sdim)
            #elif M < N:
            #    idx = np.arange(y - Sdim + 1, Ldim)
        else:
            idx = np.arange(y - N + 1, M)
            blk[idx, y - idx] = I[k:k + idx.shape[0]]
            k += idx.shape[0]
            #I = np.hstack((I, blk[idx, y - idx]))
            #if M > N:
            #    idx = np.arange(y - Sdim + 1, Ldim)
            #elif M < N:
            #    idx = np.arange((y - Ldim + 1, Sdim))
                
    blk[M - 1, N - 1] = I[M*N - 1]
    
    return blk
    #I = np.hstack((I, blk[M - 1, N - 1]))

def decoding(I, sh):
    M, N = sh
    bdct = zigzag_re(I, M, N)
    blk = idct2(bdct)
    return blk
#def ret_coeffs(b_lin, nor):
#    b_lin[nor:] = 0
#    return b_lin