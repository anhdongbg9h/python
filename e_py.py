# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 23:19:40 2019

@author: haido
"""
def factorial(n):
    result=1
    for e in range(2,n+1):
        result= result*e
    return result

def estimate_e(n):
    result=1
    for e in range(1,n+1):
        result= result+1/factorial(e)
    return result
print(estimate_e(10))