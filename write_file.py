# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 23:53:06 2019

@author: haido
"""

import os
file_path='my_file.txt'

check1=os.path.exists(file_path)

print(check1)

file_path=open(file_path,'w')
text='Hoc Vien Ky Thuat Quan Su'

file_path.write(text)

file_path.close()
