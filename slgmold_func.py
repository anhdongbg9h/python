# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 10:30:38 2019

@author: haido
"""

import math

def slgmold_function(data):
    result=[]
    for d in data:
        result.append(1/(1+math.exp(-d)))
    return result

data=[1,5,-4,3,-2]

result=slgmold_function(data)
print(result)