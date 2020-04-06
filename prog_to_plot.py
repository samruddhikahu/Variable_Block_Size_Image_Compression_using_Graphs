#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 23:25:42 2019

@author: samruddhi
"""

import matplotlib as mpl
#import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
df_dct = pd.read_csv('/home/samruddhi/GSP_Compression/No_coeffs_vs_msepsnr_dct.csv')
df_gft = pd.read_csv('/home/samruddhi/GSP_Compression/No_coeffs_vs_msepsnr_gft.csv')
nc = df_dct["no_coeffs"]
mse_dct = df_dct["mse"]
psnr_dct = df_dct["psnr"]
mse_gft = df_gft["mse"]
psnr_gft = df_gft["psnr"]
font = {'family': 'normal',
'weight':'bold',
'size': 22}
mpl.rc('font', **font)
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)

ax.plot(nc, psnr_dct, 'r-o', nc, psnr_gft, 'b-*', linewidth=3)
plt.gca().legend(('DCT', 'GFT'))
plt.ylabel('PSNR (dB)')
plt.xlabel('No. of retained coefficients')
plt.grid(True)
plt.show()
#plt.plot(nc, mse_dct, 'r-o', nc, mse_gft, 'b-*')
#plt.gca().legend(('DCT', 'GFT'))
#plt.xlabel('No. of retained coefficients')
#plt.ylabel('Mean Square Error')
#plt.grid(True)