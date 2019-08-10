# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 11:08:54 2019

@author: haido
"""

#import math

def Relu_function(data):
    result=[]
    for d in data:
        if d<0:
            result.append(0)
        else:
            result.append(d)
    return result

data=[1,5,-4,3,-2]

result=Relu_function(data)
print(result)