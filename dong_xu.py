# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 00:18:33 2019

@author: haido
"""

import random

# Tổng số lần búng đồng xu
total_flips = 0  

# số lần mặt sau xuất hiện
num_ngua = 0

# số lần mặt trước xuất hiện
num_sap = 0

for _ in range(1000):
    # sinh số ngẫu nhiên nằm trong khoảng [0,1)
    n = random.randint(1,7)*1/10
    if n < 0.5:
        num_ngua = num_ngua + 1
    else:
        num_sap = num_sap + 1
    
    # code ở vị trí này không thuộc khối else    
    total_flips = total_flips + 1
    
# code ở ví trị này không thuộc khối code cho for
# vòng lặp for đã thực hiên xong
print('total_flips: %d' % total_flips)
print('num_ngua: %d' % num_ngua)
print('num_sap: %d' % num_sap)
