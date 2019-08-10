# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 09:48:56 2019

@author: haido
"""

def add_vectors(vector1,vecter2):
    return [v1+v2 for v1,v2 in zip(vector1,vector2)]

vector1=[1,2]
vector2=[3,4]

added_vectors=add_vectors(vector1,vector2)
print(added_vectors)