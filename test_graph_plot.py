#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 12:40:10 2019

@author: samruddhi
"""

import matplotlib.pyplot as plt
from skimage import data, img_as_float
import pygsp as pygsp
img = img_as_float(data.camera()[::64, ::64])
G = pygsp.graphs.ImgPatches(img, patch_shape=(3, 3))
print('{} nodes ({} x {} pixels)'.format(G.Xin.shape[0], *img.shape))
#64 nodes (8 x 8 pixels)
print('{} features per node'.format(G.Xin.shape[1]))
#9 features per node
G.set_coordinates(kind='spring', seed=42)
fig, axes = plt.subplots(1, 2)
_ = axes[0].spy(G.W, markersize=2)
G.plot(ax=axes[1])