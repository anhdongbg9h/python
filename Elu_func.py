# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 11:16:44 2019

@author: haido
"""
import math

def Elu_function(data):
    result=[]
    for d in data:
        if d<0:
            result.append(0.1*(math.exp(d)-1))
        else:
            result.append(d)
    return result

data=[1,5,-4,3,-2]

result=Elu_function(data)
print(result)