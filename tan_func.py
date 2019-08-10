# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 11:04:29 2019

@author: haido
"""

import math

def tan_function(data):
    result=[]
    for d in data:
        result.append(2/(1+math.exp(-2*d))-1)
    return result

data=[1,5,-4,3,-2]

result=tan_function(data)
print(result)