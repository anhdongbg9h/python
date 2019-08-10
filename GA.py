# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 22:37:52 2019

@author: haido
"""

import random
m=10
n=6
def generate_random_value() :
    return random.randint(0,1)

def create_individual():
    return [generate_random_value() for _ in range(n)]

population=[create_individual() for _ in range(m)]

for e in population:
    print(e)