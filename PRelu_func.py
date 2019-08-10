# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 11:14:23 2019

@author: haido
"""

def PRelu_function(data):
    result=[]
    for d in data:
        if d<0:
            result.append(0.1*d)
        else:
            result.append(d)
    return result

data=[1,5,-4,3,-2]

result=PRelu_function(data)
print(result)