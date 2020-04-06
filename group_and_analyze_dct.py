#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 17:48:24 2019

@author: samruddhi
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 15:02:24 2019

@author: samruddhi
"""
import numpy as np
import functions as fn
#from Quantization import CSF_Quantization
#from binary_arithmetic_coding import Arithmetic_Coding

def group_and_analyze(C, Idx, flag, nor):
    m, n = C.shape
    if flag == 1:
        sh = 128
    else:
        sh = 0
    #blksz = np.zeros((int(m/8), int(n/8)))
    lbl_y = np.zeros((int(m/8), int(n/8)), dtype=int)
    #Seq_acy = []
    #dc_y = []
    coeff_list = []
    #lbl_arr_y = []
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
            if i < int(m/8) - 3 and j < int(n/8) - 3 and fn.check(Idx[i:i+4, j:j+4]) and np.count_nonzero(lbl_y[i:i+4,j:j+4]) == 0: #32x32
                #tf = fn.check(Idx[i:i+4, j:j+4])
                #if tf == True:
                lbl_y[i:i+4, j:j+4] = 16
                #lbl_arr_y.append(16)
                #a1 = 8*i
                #b1 = 8*(i+4)
                #a2 = 8*j
                #b2 = 8*(j+4)
                blk = C[8*i:8*(i+4), 8*j:8*(j+4)]
                #Seq, dc = CSF_Quant_Arithmetic_QM(blk, const, flag)
                j += 4
            elif i < int(m/8) - 3 and j < int(n/8) - 2 and fn.check(Idx[i:i+4, j:j+3]) and np.count_nonzero(lbl_y[i:i+4,j:j+3]) == 0: #32x24
                #tf = fn.check(Idx[i:i+4, j:j+3])
                #if tf == True:
                lbl_y[i:i+4, j:j+3] = 15
                #lbl_arr_y.append(15)
                #a1 = 8*i
                #b1 = 8*(i+4)
                #a2 = 8*j
                #b2 = 8*(j+3)
                blk = C[8*i:8*(i+4), 8*j:8*(j+3)]
                #Seq, dc = CSF_Quant_Arithmetic_QM(blk, const, flag)
                j += 3
            elif i < int(m/8) - 2 and j < int(n/8) - 3 and fn.check(Idx[i:i+3, j:j+4]) and np.count_nonzero(lbl_y[i:i+3,j:j+4]) == 0: #24x32
                #tf = fn.check(Idx[i:i+3, j:j+4])
                #if tf == True:
                lbl_y[i:i+3, j:j+4] = 14
                #lbl_arr_y.append(14)
                #a1 = 8*i
                #b1 = 8*(i+3)
                #a2 = 8*j
                #b2 = 8*(j+4)
                blk = C[8*i:8*(i+3), 8*j:8*(j+4)]
                #Seq, dc = CSF_Quant_Arithmetic_QM(blk, const, flag)
                j += 4
            elif i < int(m/8) - 2 and j < int(n/8) - 2 and fn.check(Idx[i:i+3, j:j+3]) and np.count_nonzero(lbl_y[i:i+3,j:j+3]) == 0:  #24x24
                #tf = fn.check(Idx[i:i+3, j:j+3])
                #if tf == True:
                lbl_y[i:i+3, j:j+3] = 13
                #lbl_arr_y.append(13)
                #a1 = 8*i
                #b1 = 8*(i+3)
                #a2 = 8*j
                #b2 = 8*(j+3)
                blk = C[8*i:8*(i+3), 8*j:8*(j+3)]
                #Seq, dc = CSF_Quant_Arithmetic_QM(blk, const, flag)
                j += 3
            elif i < int(m/8) - 3 and j < int(n/8) - 1 and fn.check(Idx[i:i+4, j:j+2]) and np.count_nonzero(lbl_y[i:i+4,j:j+2]) == 0: #32x16
                #tf = fn.check(Idx[i:i+4, j:j+2])
                #if tf == True:
                lbl_y[i:i+4, j:j+2] = 12
                #lbl_arr_y.append(12)
                #a1 = 8*i
                #b1 = 8*(i+4)
                #a2 = 8*j
                #b2 = 8*(j+2)
                blk = C[8*i:8*(i+4), 8*j:8*(j+2)]
                #Seq, dc = CSF_Quant_Arithmetic_QM(blk, const, flag)
                j += 2
            elif i < int(m/8) - 1 and j < int(n/8) - 3 and fn.check(Idx[i:i+2, j:j+4]) and np.count_nonzero(lbl_y[i:i+2,j:j+4]) == 0: #16x32
                #tf = fn.check(Idx[i:i+2, j:j+4])
                #if tf == True:
                lbl_y[i:i+2, j:j+4] = 11
                #lbl_arr_y.append(11)
                #a1 = 8*i
                #b1 = 8*(i+2)
                #a2 = 8*j
                #b2 = 8*(j+4)
                blk = C[8*i:8*(i+2), 8*j:8*(j+4)]
                #Seq, dc = CSF_Quant_Arithmetic_QM(blk, const, flag)
                j += 4
            elif i < int(m/8) - 2 and j < int(n/8) - 1 and fn.check(Idx[i:i+3, j:j+2]) and np.count_nonzero(lbl_y[i:i+3,j:j+2]) == 0:  #24x16
                #tf = fn.check(Idx[i:i+3, j:j+2])
                #if tf == True:
                lbl_y[i:i+3, j:j+2] = 10
                #lbl_arr_y.append(10)
                #a1 = 8*i
                #b1 = 8*(i+3)
                #a2 = 8*j
                #b2 = 8*(j+2)
                blk = C[8*i:8*(i+3), 8*j:8*(j+2)]
                #Seq, dc = CSF_Quant_Arithmetic_QM(blk, const, flag)
                j += 2
            elif i < int(m/8) - 1 and j < int(n/8) - 2 and fn.check(Idx[i:i+2, j:j+3]) and np.count_nonzero(lbl_y[i:i+2,j:j+3]) == 0:  #16x24
                #tf = fn.check(Idx[i:i+2, j:j+3])
                #if tf == True:
                lbl_y[i:i+2, j:j+3] = 9
                #lbl_arr_y.append(9)
                #a1 = 8*i
                #b1 = 8*(i+2)
                #a2 = 8*j
                #b2 = 8*(j+3)
                blk = C[8*i:8*(i+2), 8*j:8*(j+3)]
                #Seq, dc = CSF_Quant_Arithmetic_QM(blk, const, flag)
                j += 3
            elif i < int(m/8) - 3 and fn.check(Idx[i:i+4, j]) and np.count_nonzero(lbl_y[i:i+4,j]) == 0: #32x8
                #tf = fn.check(Idx[i:i+4, j])
                #if tf == True:
                lbl_y[i:i+4, j] = 8
                #lbl_arr_y.append(8)
                #a1 = 8*i
                #b1 = 8*(i+4)
                #a2 = 8*j
                #b2 = 8*(j+1)
                blk = C[8*i:8*(i+4), 8*j:8*(j+1)]
                #Seq, dc = CSF_Quant_Arithmetic_QM(blk, const, flag)
                j += 1 
            elif i < int(m/8) - 1 and j < int(n/8) - 1 and fn.check(Idx[i:i+2, j:j+2]) and np.count_nonzero(lbl_y[i:i+2,j:j+2]) == 0:  #16x16
                #tf = fn.check(Idx[i:i+2, j:j+2])
                #if tf == True:
                lbl_y[i:i+2, j:j+2] = 7
                #lbl_arr_y.append(7)
                #a1 = 8*i
                #b1 = 8*(i+2)
                #a2 = 8*j
                #b2 = 8*(j+2)
                blk = C[8*i:8*(i+2), 8*j:8*(j+2)]
                #Seq, dc = CSF_Quant_Arithmetic_QM(blk, const, flag)
                j += 2
            elif j < int(n/8) - 3 and fn.check(Idx[i, j:j+4]) and np.count_nonzero(lbl_y[i,j:j+4]) == 0: #8x32
                #tf = fn.check(Idx[i, j:j+4])
                #if tf == True:
                lbl_y[i, j:j+4] = 6
                #lbl_arr_y.append(6)
                #a1 = 8*i
                #b1 = 8*(i+1)
                #a2 = 8*j
                #b2 = 8*(j+4)
                blk = C[8*i:8*(i+1), 8*j:8*(j+4)]
                #Seq, dc = CSF_Quant_Arithmetic_QM(blk, const, flag)
                j += 4
            elif i < int(m/8) - 2 and fn.check(Idx[i:i+3, j]) and np.count_nonzero(lbl_y[i:i+3,j]) == 0: #24x8
                #tf = fn.check(Idx[i:i+3, j])
                #if tf == True:
                lbl_y[i:i+3, j] = 5
                #lbl_arr_y.append(5)
                #a1 = 8*i
                #b1 = 8*(i+3)
                #a2 = 8*j
                #b2 = 8*(j+1)
                blk = C[8*i:8*(i+3), 8*j:8*(j+1)]
                #Seq, dc = CSF_Quant_Arithmetic_QM(blk, const, flag)
                j += 1
            elif j < int(n/8) - 2 and fn.check(Idx[i, j:j+3]) and np.count_nonzero(lbl_y[i,j:j+3]) == 0: #8x24
                #tf = fn.check(Idx[i, j:j+3])
                #if tf == True:
                lbl_y[i, j:j+3] = 4
                #lbl_arr_y.append(4)
                #a1 = 8*i
                #b1 = 8*(i+1)
                #a2 = 8*j
                #b2 = 8*(j+3)
                blk = C[8*i:8*(i+1), 8*j:8*(j+3)]
                #Seq, dc = CSF_Quant_Arithmetic_QM(blk, const, flag)
                j += 3
            elif i < int(m/8) - 1 and fn.check(Idx[i:i+2, j]) and np.count_nonzero(lbl_y[i:i+2,j]) == 0: #16x8
                #tf = fn.check(Idx[i:i+2, j])
                #if tf == True:
                lbl_y[i:i+2, j] = 3
                #lbl_arr_y.append(3)
                #a1 = 8*i
                #b1 = 8*(i+2)
                #a2 = 8*j
                #b2 = 8*(j+1)
                blk = C[8*i:8*(i+2), 8*j:8*(j+1)]
                #Seq, dc = CSF_Quant_Arithmetic_QM(blk, const, flag)
                j += 1
            elif j < int(n/8) - 1 and fn.check(Idx[i, j:j+2]) and np.count_nonzero(lbl_y[i,j:j+2]) == 0: #8x16
                #tf = fn.check(Idx[i, j:j+2])
                #if tf == True:
                lbl_y[i, j:j+2] = 2
                #lbl_arr_y.append(2)
                #a1 = 8*i
                #b1 = 8*(i+1)
                #a2 = 8*j
                #b2 = 8*(j+2)
                blk = C[8*i:8*(i+1), 8*j:8*(j+2)]
                #Seq, dc = CSF_Quant_Arithmetic_QM(blk, const, flag)
                j += 2
            else:                                                            #8x8
                lbl_y[i,j] = 1
                #lbl_arr_y.append(1)
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
            #bquant = CSF_Quantization(bdct, const)
            bquant = np.round(bdct)
            #Zigzag Ordering:-
            b_lin = fn.zigzag(bquant)
            b_lin[nor:] = 0
            #Arithmetic QM Coding:-
            #Seq, dc = Arithmetic_Coding(b_lin)
            coeff_list.append(b_lin)
            
            #Seq_acy.append(Seq)
            #dc_y.append(dc)
            
        i += 1
        
    return coeff_list, lbl_y

def degroup_and_decode(coeff_list, lbl_y):
    m, n = np.shape(lbl_y)
    CYrec = np.zeros((int(m*8), int(n*8)))
    
    i = 0
    while np.count_nonzero(lbl_y) > 0:
        j = 0
        while j < n:
            try:
                #r = np.amin(np.where(lbl_y[:,j] == 0))
                r = np.amin(np.nonzero(lbl_y[:,j]))
            except ValueError:
                j += 1
                continue
            i = r
            if lbl_y[i, j] == 1:           #8x8
                #coeffs = coeff_list[0]
                blk = fn.decoding(coeff_list[0], [8, 8])
                #a1 = 8*i
                #b1 = 8*(i+1)
                #a2 = 8*j
                #b2 = 8*(j+1)
                CYrec[8*i:8*(i+1), 8*j:8*(j+1)] = blk
                lbl_y[i, j] = 0
                coeff_list.pop(0)
                #W_list.pop(0)
                j += 1
            elif lbl_y[i, j] == 2:        #8x16
                #coeffs = coeff_list[0]
                blk = fn.decoding(coeff_list[0], [8, 16])
                #a1 = 8*i
                #b1 = 8*(i+1)
                #a2 = 8*j
                #b2 = 8*(j+2)
                CYrec[8*i:8*(i+1), 8*j:8*(j+2)] = blk
                lbl_y[i, j:j+2] = 0
                coeff_list.pop(0)
                #W_list.pop(0)
                j += 2
            elif lbl_y[i, j] == 3:       #16x8
                #coeffs = coeff_list[0]
                blk = fn.decoding(coeff_list[0], [16, 8])
                #a1 = 8*i
                #b1 = 8*(i+2)
                #a2 = 8*j
                #b2 = 8*(j+1)
                CYrec[8*i:8*(i+2), 8*j:8*(j+1)] = blk
                lbl_y[i:i+2, j] = 0
                coeff_list.pop(0)
                #W_list.pop(0)
                j += 1
            elif lbl_y[i, j] == 4:        #8x24
                #coeffs = coeff_list[0]
                blk = fn.decoding(coeff_list[0], [8, 24])
                #a1 = 8*i
                #b1 = 8*(i+1)
                #a2 = 8*j
                #b2 = 8*(j+3)
                CYrec[8*i:8*(i+1), 8*j:8*(j+3)] = blk
                lbl_y[i, j:j+3] = 0
                coeff_list.pop(0)
                
                j += 3
            elif lbl_y[i, j] == 5:       #24x8
                #coeffs = coeff_list[0]
                blk = fn.decoding(coeff_list[0], [24, 8])
                #a1 = 8*i
                #b1 = 8*(i+3)
                #a2 = 8*j
                #b2 = 8*(j+1)
                CYrec[8*i:8*(i+3), 8*j:8*(j+1)] = blk
                lbl_y[i:i+3, j] = 0
                coeff_list.pop(0)
                
                j += 1
            elif lbl_y[i, j] == 6:        #8x32
                #coeffs = coeff_list[0]
                blk = fn.decoding(coeff_list[0], [8, 32])
                #a1 = 8*i
                #b1 = 8*(i+1)
                #a2 = 8*j
                #b2 = 8*(j+4)
                CYrec[8*i:8*(i+1), 8*j:8*(j+4)] = blk
                lbl_y[i, j:j+4] = 0
                coeff_list.pop(0)
                
                j += 4
            elif lbl_y[i, j] == 7:       #16x16
                #coeffs = coeff_list[0]
                blk = fn.decoding(coeff_list[0], [16, 16])
                #a1 = 8*i
                #b1 = 8*(i+2)
                #a2 = 8*j
                #b2 = 8*(j+2)
                CYrec[8*i:8*(i+2), 8*j:8*(j+2)] = blk
                lbl_y[i:i+2, j:j+2] = 0
                coeff_list.pop(0)
                
                j += 2
            elif lbl_y[i, j] == 8:       #32x8
                #coeffs = coeff_list[0]
                blk = fn.decoding(coeff_list[0], [32, 8])
                #a1 = 8*i
                #b1 = 8*(i+4)
                #a2 = 8*j
                #b2 = 8*(j+1)
                CYrec[8*i:8*(i+4), 8*j:8*(j+1)] = blk
                lbl_y[i:i+4, j] = 0
                coeff_list.pop(0)
                
                j += 1
            elif lbl_y[i, j] == 9:        #16x24
                #coeffs = coeff_list[0]
                blk = fn.decoding(coeff_list[0], [16, 24])
                #a1 = 8*i
                #b1 = 8*(i+2)
                #a2 = 8*j
                #b2 = 8*(j+3)
                CYrec[8*i:8*(i+2), 8*j:8*(j+3)] = blk
                lbl_y[i:i+2, j:j+3] = 0
                coeff_list.pop(0)
                #W_list.pop(0)
                j += 3
            elif lbl_y[i, j] == 10:       #24x16
                #coeffs = coeff_list[0]
                blk = fn.decoding(coeff_list[0], [24, 16])
                #a1 = 8*i
                #b1 = 8*(i+3)
                #a2 = 8*j
                #b2 = 8*(j+2)
                CYrec[8*i:8*(i+3), 8*j:8*(j+2)] = blk
                lbl_y[i:i+3, j:j+2] = 0
                coeff_list.pop(0)
                #W_list.pop(0)
                j += 2
            elif lbl_y[i, j] == 11:        #16x32
                #coeffs = coeff_list[0]
                blk = fn.decoding(coeff_list[0], [16, 32])
                #a1 = 8*i
                #b1 = 8*(i+2)
                #a2 = 8*j
                #b2 = 8*(j+4)
                CYrec[8*i:8*(i+2), 8*j:8*(j+4)] = blk
                lbl_y[i:i+2, j:j+4] = 0
                coeff_list.pop(0)
                #W_list.pop(0)
                j += 4
            elif lbl_y[i, j] == 12:       #32x16
                #coeffs = coeff_list[0]
                blk = fn.decoding(coeff_list[0], [32, 16])
                #a1 = 8*i
                #b1 = 8*(i+4)
                #a2 = 8*j
                #b2 = 8*(j+2)
                CYrec[8*i:8*(i+4), 8*j:8*(j+2)] = blk
                lbl_y[i:i+4, j:j+2] = 0
                coeff_list.pop(0)
#                
                j += 2
            elif lbl_y[i, j] == 13:       #24x24
                #coeffs = coeff_list[0]
                blk = fn.decoding(coeff_list[0], [24, 24])
                #a1 = 8*i
                #b1 = 8*(i+3)
                #a2 = 8*j
                #b2 = 8*(j+3)
                CYrec[8*i:8*(i+3), 8*j:8*(j+3)] = blk
                lbl_y[i:i+3, j:j+3] = 0
                coeff_list.pop(0)
                
                j += 3
            elif lbl_y[i, j] == 14:       #24x32
                #coeffs = coeff_list[0]
                blk = fn.decoding(coeff_list[0], [24, 32])
                #a1 = 8*i
                #b1 = 8*(i+3)
                #a2 = 8*j
                #b2 = 8*(j+4)
                CYrec[8*i:8*(i+3), 8*j:8*(j+4)] = blk
                lbl_y[i:i+3, j:j+4] = 0
                coeff_list.pop(0)
                
                j += 4
            elif lbl_y[i, j] == 15:       #32x24
                #coeffs = coeff_list[0]
                blk = fn.decoding(coeff_list[0], [32, 24])
                #a1 = 8*i
                #b1 = 8*(i+4)
                #a2 = 8*j
                #b2 = 8*(j+3)
                CYrec[8*i:8*(i+4), 8*j:8*(j+3)] = blk
                lbl_y[i:i+4, j:j+3] = 0
                coeff_list.pop(0)
#                
                j += 3
            elif lbl_y[i, j] == 16:       #32x32
                #coeffs = coeff_list[0]
                blk = fn.decoding(coeff_list[0], [32, 32])
                #a1 = 8*i
                #b1 = 8*(i+4)
                #a2 = 8*j
                #b2 = 8*(j+4)
                CYrec[8*i:8*(i+4), 8*j:8*(j+4)] = blk
                lbl_y[i:i+4, j:j+4] = 0
                coeff_list.pop(0)
                
                j += 4
    
    return CYrec + 128
    
            