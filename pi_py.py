# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 23:19:50 2019

@author: haido
"""

import random
import math

N=100000
N_T=0
for e in range(N):
    x=random.random()*2-1
    y=random.random()*2-1
    
    x2=x**2
    y2=y**2
    
    if math.sqrt(x2+y2)<1.0:
        N_T=N_T+1

pi=(N_T/N)*4

print(pi)