# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 21:06:47 2022

@author: DELL
"""
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('histo.jpeg',0)
plt.figure(figsize=(10,10))                      
plt.imshow(img) 
equ = cv.equalizeHist(img)
res = np.hstack((img,equ))
cv.imwrite('res.png',res)
plt.plot(equ)
plt.show()
plt.figure(figsize=(10,10))                      
plt.imshow(equ) 
