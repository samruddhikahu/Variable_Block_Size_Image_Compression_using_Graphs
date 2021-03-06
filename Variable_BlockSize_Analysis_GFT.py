#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 09:57:50 2019

@author: samruddhi
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 18:31:40 2019

@author: samruddhi
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 14:32:06 2019

@author: samruddhi
"""

import numpy as np
#import matplotlib.pyplot as plt
#import matplotlib.image as mpimg
#from PIL import Image
#from RGB_to_YCbCr_Conversion import rgb2ycbcr
from histogram_and_index import hist_and_ind
from group_and_analyze_gft import group_and_analyze, degroup_and_decode
import functions as fn
import pandas as pd
import cv2

#from scipy.io import loadmat
#
#CYmat = loadmat('CY.mat')
#Cbmat = loadmat('CCb.mat')
#Crmat = loadmat('CCr.mat')

#A = Image.open("Image14.bmp")

A = cv2.imread('Image14.bmp')
#plt.imshow(A)
cv2.imshow('Original Image', A)
#cv2.waitkey(0)
#plt.title('Original Image')
#m, n = A.size


# Converting to YCbCr:-
#B = rgb2ycbcr(A)    
#B = B.astype(np.uint8)
B = cv2.cvtColor(A, cv2.COLOR_BGR2YCR_CB)
#cv2.imshow('YCbCr Image', B[:,:,(0,2,1)])
#cv2.waitkey(0)

#C = cv2.cvtColor(A, cv2.COLOR_BGR2LAB)
#cv2.imshow('CIE L*a*b* Image', C)

CY = B[:,:,0]
cv2.imshow('Y Plane', CY)
CCb = B[:,:,2]
CCr = B[:,:,1]

#cv2.imshow('Y Plane', CY)
#cv2.imshow('MATLAB Y Plane', CYmat['CY'])
#cv2.imshow('Cb Plane', CCb)
#cv2.imshow('MATLAB Cb Plane', Cbmat['CCb'])
#cv2.imshow('Cr Plane', CCr)
#cv2.imshow('MATLAB Cr Plane', Crmat['CCr'])
#Fname = quantization_matrix_adaptive_ksii(const)
const = -0.5
######################### Coding the Y Plane #################################
CY = CY.astype(np.int16)
#Formation of the index matrix using a histogram:-
Idx = hist_and_ind(CY)

#Grouping and Coding of the image blocks:-
#k = 0
mse_list = []
psnr_list = []
#for n in range(1, 1024, 16):
#noret = n #1024  # No. of retained coefficients
coeff_list, W_list, lbl_y = group_and_analyze(CY, Idx, 1) #, noret)
        
#df = pd.DataFrame(data=coeff_list)
#df.to_csv('Variable_BlockSize_GFT_Coeffs.csv')

###################### Decoding the Y Plane ##################################
CYrec = degroup_and_decode(coeff_list, W_list, lbl_y)
cv2.imshow('Reconstructed Y Plane', CYrec.astype(np.uint8))

mse, psnr = fn.calc_mse_psnr(CY, CYrec)
mse_list.append(mse)
psnr_list.append(psnr)
#k += 1

#d = {'no_coeffs' : np.arange(1, 1024, 16), 'mse' : mse_list, 'psnr' : psnr_list}
#df = pd.DataFrame(data=d)
#df.to_csv('No_coeffs_vs_msepsnr_gftw.csv')