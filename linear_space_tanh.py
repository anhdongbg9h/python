# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 13:11:04 2019

@author: haido
"""

import math
import matplotlib.pyplot as plt

def tanh_function(data):
    return [(math.exp(x)-math.exp(-x))/(math.exp(x)+math.exp(-x)) for x in data]

def linear_space(start,stop,num=10):
    num=int(num)
    start=start*1
    stop=stop*1
    assert num>1,'num lon hon 1'
    
    step=(stop-start)/num
    result=[]
    for e in range(num):
        result.append(start+step*e)
    return result
#t=linear_space(1,10,5)
#print(t)
plt.xlabel('x values')
plt.ylabel('y values')
data=linear_space(-5,5,100)
data_tanh=tanh_function(data)
plt.plot(data,data_tanh,color="#d35400")
plt.show()
#print(a)