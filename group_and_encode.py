#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 15:02:24 2019

@author: samruddhi
"""
import numpy as np
import functions as fn
from Quantization import CSF_Quantization
from binary_arithmetic_coding import Arithmetic_Coding

def group_and_code(C, Idx, const, flag):
    m, n = C.shape
    if flag == 1:
        sh = 128
    else:
        sh = 0
    #blksz = np.zeros((int(m/8), int(n/8)))
    lbl_y = np.zeros((int(m/8), int(n/8)))
    Seq_acy = []
    dc_y = []
    lbl_arr_y = []
    while np.amin(lbl_y) == 0:
        j = 0
        while j < int(n/8):
            # Seq = []
            try:
                r = np.amin(np.where(lbl_y[:,j] == 0))
            except ValueError:
                j += 1
                continue
            i = r
            if i < int(m/8) - 3 and j < int(n/8) - 3 and np.count_nonzero(lbl_y[i:i+4,j:j+4]) == 0: #32x32
                tf = fn.check(Idx[i:i+4, j:j+4])
                if tf == True:
                    lbl_y[i:i+4, j:j+4] = 16
                    lbl_arr_y.append(16)
                    #a1 = 8*i
                    #b1 = 8*(i+4)
                    #a2 = 8*j
                    #b2 = 8*(j+4)
                    blk = C[8*i:8*(i+4), 8*j:8*(j+4)]
                    #Seq, dc = CSF_Quant_Arithmetic_QM(blk, const, flag)
                    j += 4
                    
            elif i < int(m/8) - 3 and j < int(n/8) - 2 and np.count_nonzero(lbl_y[i:i+4,j:j+3]) == 0: #32x24
                tf = fn.check(Idx[i:i+4, j:j+3])
                if tf == True:
                    lbl_y[i:i+4, j:j+3] = 15
                    lbl_arr_y.append(15)
                    #a1 = 8*i
                    #b1 = 8*(i+4)
                    #a2 = 8*j
                    #b2 = 8*(j+3)
                    blk = C[8*i:8*(i+4), 8*j:8*(j+3)]
                    #Seq, dc = CSF_Quant_Arithmetic_QM(blk, const, flag)
                    j += 3
                    
            elif i < int(m/8) - 2 and j < int(n/8) - 3 and np.count_nonzero(lbl_y[i:i+3,j:j+4]) == 0: #24x32
                tf = fn.check(Idx[i:i+3, j:j+4])
                if tf == True:
                    lbl_y[i:i+3, j:j+4] = 14
                    lbl_arr_y.append(14)
                    #a1 = 8*i
                    #b1 = 8*(i+3)
                    #a2 = 8*j
                    #b2 = 8*(j+4)
                    blk = C[8*i:8*(i+3), 8*j:8*(j+4)]
                    #Seq, dc = CSF_Quant_Arithmetic_QM(blk, const, flag)
                    j += 4
                    
            elif i < int(m/8) - 2 and j < int(n/8) - 2 and np.count_nonzero(lbl_y[i:i+3,j:j+3]) == 0:  #24x24
                tf = fn.check(Idx[i:i+3, j:j+3])
                if tf == True:
                    lbl_y[i:i+3, j:j+3] = 13
                    lbl_arr_y.append(13)
                    #a1 = 8*i
                    #b1 = 8*(i+3)
                    #a2 = 8*j
                    #b2 = 8*(j+3)
                    blk = C[8*i:8*(i+3), 8*j:8*(j+3)]
                    #Seq, dc = CSF_Quant_Arithmetic_QM(blk, const, flag)
                    j += 3
                    
            elif i < int(m/8) - 3 and j < int(n/8) - 1 and np.count_nonzero(lbl_y[i:i+4,j:j+2]) == 0: #32x16
                tf = fn.check(Idx[i:i+4, j:j+2])
                if tf == True:
                    lbl_y[i:i+4, j:j+2] = 12
                    lbl_arr_y.append(12)
                    #a1 = 8*i
                    #b1 = 8*(i+4)
                    #a2 = 8*j
                    #b2 = 8*(j+2)
                    blk = C[8*i:8*(i+4), 8*j:8*(j+2)]
                    #Seq, dc = CSF_Quant_Arithmetic_QM(blk, const, flag)
                    j += 2
                    
            elif i < int(m/8) - 1 and j < int(n/8) - 3 and np.count_nonzero(lbl_y[i:i+2,j:j+4]) == 0: #16x32
                tf = fn.check(Idx[i:i+2, j:j+4])
                if tf == True:
                    lbl_y[i:i+2, j:j+4] = 11
                    lbl_arr_y.append(11)
                    #a1 = 8*i
                    #b1 = 8*(i+2)
                    #a2 = 8*j
                    #b2 = 8*(j+4)
                    blk = C[8*i:8*(i+2), 8*j:8*(j+4)]
                    #Seq, dc = CSF_Quant_Arithmetic_QM(blk, const, flag)
                    j += 4
                    
            elif i < int(m/8) - 2 and j < int(n/8) - 1 and np.count_nonzero(lbl_y[i:i+3,j:j+2]) == 0:  #24x16
                tf = fn.check(Idx[i:i+3, j:j+2])
                if tf == True:
                    lbl_y[i:i+3, j:j+2] = 10
                    lbl_arr_y.append(10)
                    #a1 = 8*i
                    #b1 = 8*(i+3)
                    #a2 = 8*j
                    #b2 = 8*(j+2)
                    blk = C[8*i:8*(i+3), 8*j:8*(j+2)]
                    #Seq, dc = CSF_Quant_Arithmetic_QM(blk, const, flag)
                    j += 2
                    
            elif i < int(m/8) - 1 and j < int(n/8) - 2 and np.count_nonzero(lbl_y[i:i+2,j:j+3]) == 0:  #16x24
                tf = fn.check(Idx[i:i+2, j:j+3])
                if tf == True:
                    lbl_y[i:i+2, j:j+3] = 9
                    lbl_arr_y.append(9)
                    #a1 = 8*i
                    #b1 = 8*(i+2)
                    #a2 = 8*j
                    #b2 = 8*(j+3)
                    blk = C[8*i:8*(i+2), 8*j:8*(j+3)]
                    #Seq, dc = CSF_Quant_Arithmetic_QM(blk, const, flag)
                    j += 3
                    
            elif i < int(m/8) - 3 and np.count_nonzero(lbl_y[i:i+4,j]) == 0: #32x8
                tf = fn.check(Idx[i:i+4, j])
                if tf == True:
                    lbl_y[i:i+4, j] = 8
                    lbl_arr_y.append(8)
                    #a1 = 8*i
                    #b1 = 8*(i+4)
                    #a2 = 8*j
                    #b2 = 8*(j+1)
                    blk = C[8*i:8*(i+4), 8*j:8*(j+1)]
                    #Seq, dc = CSF_Quant_Arithmetic_QM(blk, const, flag)
                    j += 1
                    
            elif i < int(m/8) - 1 and j < int(n/8) - 1 and np.count_nonzero(lbl_y[i:i+2,j:j+2]) == 0:  #16x16
                tf = fn.check(Idx[i:i+2, j:j+2])
                if tf == True:
                    lbl_y[i:i+2, j:j+2] = 7
                    lbl_arr_y.append(7)
                    #a1 = 8*i
                    #b1 = 8*(i+2)
                    #a2 = 8*j
                    #b2 = 8*(j+2)
                    blk = C[8*i:8*(i+2), 8*j:8*(j+2)]
                    #Seq, dc = CSF_Quant_Arithmetic_QM(blk, const, flag)
                    j += 2
                    
            elif j < int(n/8) - 3 and np.count_nonzero(lbl_y[i,j:j+4]) == 0: #8x32
                tf = fn.check(Idx[i, j:j+4])
                if tf == True:
                    lbl_y[i, j:j+4] = 6
                    lbl_arr_y.append(6)
                    #a1 = 8*i
                    #b1 = 8*(i+1)
                    #a2 = 8*j
                    #b2 = 8*(j+4)
                    blk = C[8*i:8*(i+1), 8*j:8*(j+4)]
                    #Seq, dc = CSF_Quant_Arithmetic_QM(blk, const, flag)
                    j += 4
                    
            elif i < int(m/8) - 2 and np.count_nonzero(lbl_y[i:i+3,j]) == 0: #24x8
                tf = fn.check(Idx[i:i+3, j])
                if tf == True:
                    lbl_y[i:i+3, j] = 5
                    lbl_arr_y.append(5)
                    #a1 = 8*i
                    #b1 = 8*(i+3)
                    #a2 = 8*j
                    #b2 = 8*(j+1)
                    blk = C[8*i:8*(i+3), 8*j:8*(j+1)]
                    #Seq, dc = CSF_Quant_Arithmetic_QM(blk, const, flag)
                    j += 1
                    
            elif j < int(n/8) - 2 and np.count_nonzero(lbl_y[i,j:j+3]) == 0: #8x24
                tf = fn.check(Idx[i, j:j+3])
                if tf == True:
                    lbl_y[i, j:j+3] = 4
                    lbl_arr_y.append(4)
                    #a1 = 8*i
                    #b1 = 8*(i+1)
                    #a2 = 8*j
                    #b2 = 8*(j+3)
                    blk = C[8*i:8*(i+1), 8*j:8*(j+3)]
                    #Seq, dc = CSF_Quant_Arithmetic_QM(blk, const, flag)
                    j += 3
                    
            elif i < int(m/8) - 1 and np.count_nonzero(lbl_y[i:i+2,j]) == 0: #16x8
                tf = fn.check(Idx[i:i+2, j])
                if tf == True:
                    lbl_y[i:i+2, j] = 3
                    lbl_arr_y.append(3)
                    #a1 = 8*i
                    #b1 = 8*(i+2)
                    #a2 = 8*j
                    #b2 = 8*(j+1)
                    blk = C[8*i:8*(i+2), 8*j:8*(j+1)]
                    #Seq, dc = CSF_Quant_Arithmetic_QM(blk, const, flag)
                    j += 1
                    
            elif j < int(n/8) - 1 and np.count_nonzero(lbl_y[i,j:j+2]) == 0: #8x16
                tf = fn.check(Idx[i, j:j+2])
                if tf == True:
                    lbl_y[i, j:j+2] = 2
                    lbl_arr_y.append(2)
                    #a1 = 8*i
                    #b1 = 8*(i+1)
                    #a2 = 8*j
                    #b2 = 8*(j+2)
                    blk = C[8*i:8*(i+1), 8*j:8*(j+2)]
                    #Seq, dc = CSF_Quant_Arithmetic_QM(blk, const, flag)
                    j += 2
                    
            else:                                                            #8x8
                lbl_y[i,j] = 1
                lbl_arr_y.append(1)
                #a1 = 8*i
                #b1 = 8*(i+1)
                #a2 = 8*j
                #b2 = 8*(j+1)
                blk = C[8*i:8*(i+1), 8*j:8*(j+1)]
                #Seq, dc = CSF_Quant_Arithmetic_QM(blk, const, flag)
                j += 1
            
            # Level Shifting and 2D-DCT:-
            bsh = blk - sh
            bdct = fn.dct2(bsh)
            #CSF based Quantization:-
            bquant = CSF_Quantization(bdct, const)
            #Zigzag Ordering:-
            b_lin = fn.zigzag(bquant)
            #Arithmetic QM Coding:-
            Seq, dc = Arithmetic_Coding(b_lin)
            
            
            Seq_acy.append(Seq)
            dc_y.append(dc)
            
        i += 1
        
    return Seq_acy, dc_y, lbl_arr_y, lbl_y


    
            