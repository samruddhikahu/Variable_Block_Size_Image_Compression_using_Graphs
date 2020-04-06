#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 10:02:06 2019

@author: samruddhi
"""

def zigzag_mn_old(blk):
    M, N = np.shape(blk)
    I = np.zeros((1, M*N))
    sm = M + N -1
    I[0] = blk[0, 0]
    z = 1
    #k = 0
    
    N1 = np.minimum(M, N)
    M1 = np.maximum(M, N)
    
    if M > N:
        for y in range(1, sm):
            if y < N1:
                if y % 2 == 1:
                    k = 0
                    while (y - k) >= 0:
                        I[z] = blk[k, y - k]
                        k += 1
                        z += 1
                else:
                    l = 0
                    while (y - l) >= 0 and y < N1:
                        I[z] = blk[y - l, l]
                        l += 1
                        z += 1
            elif y >= N1 and y < M1:
                if y % 2 == 1:
                    k = y - N1 + 1
                    while (y - k) >= 0:
                        I[z] = blk[k, y - k]
                        k += 1
                        z += 1
                else:
                    while (y - l) >= 0 and l < N1:
                        I[z] = blk[y - l, l]
                        l += 1
                        z += 1
            else:
                if y % 2 == 1:
                    k = y - N1 + 1
                    while (y - k) >= 0 and k <= M1:
                        I[z] = blk[k, y - k]
                        k += 1
                        z += 1
                else:
                    #l = M
                    k = y - M1 + 1
                    while (y - k) >= 0 and k < N1:
                        I[z] = blk[y - k, k]
                        k += 1
                        z += 1
    elif M < N:
        for y in range(1, sm):
            if y < N1:
                if y % 2 == 1:
                    k = 0
                    while (y - k) >= 0:
                        I[z] = blk[k, y - k]
                        k += 1
                        z += 1
                else:
                    l = 0
                    while (y - l) >= 0 and y < N1:
                        I[z] = blk[y - l, l]
                        l += 1
                        z += 1
            elif y >= N1 and y < M1:
                if y % 2 == 1:
                    k = 0
                    while (y - k) >= 0 and y < M1:
                        I[z] = blk[k, y - k]
                        k += 1
                        z += 1
                else:
                    l = y - N1 + 1
                    while (y - l) >= 0:
                        I[z] = blk[y - l, l]
                        l += 1
                        z += 1
            else:
                if y % 2 == 1:
                    k = y - N + 1
                    while (y - k) >= 0 and k < N1:
                        I[z] = blk[k, y-k]
                        k += 1
                        z += 1
                else:
                    k = y - M + 1
                    while (y - k) >= 0 and k < M1:
                        I[z] = blk[y - k, k]
                        k += 1
                        z += 1
    else:
        for y in range(1, sm):
            if y < N1:
                if y % 2 == 1:
                    k = 0
                    while (y - k) >= 0:
                        I[z] = blk[k, y - k]
                        k += 1
                        z += 1
                else:
                    l = 0
                    while (y - l) >= 0:
                        I[z] = blk[y - l, l]
                        l += 1
                        z += 1
            else:
                if y % 2 == 1:
                    k = y - M1 + 1
                    while (M1 - k - 1) >= 0:
                        I[z] = blk[k, y - k]
                        k += 1
                        z += 1
                else:
                    l = y - N1 + 1
                    while (N1 - l - 1) >= 0:
                        I[z] = blk[y - l, l]
                        l += 1
                        z += 1
    I[z] = blk[M, N]
    
    return I