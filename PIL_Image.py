# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 16:47:43 2019

@author: haido
"""
from PIL import Image
#a=Image.open("JW_3.jpg")
im= Image.open('Sydney-Opera-House.jpg')
print(im.format,im.size,im.mode)
out=im.resize((128,128))
out=im.rotate(90)

im.show()
out.show()
#a.show()