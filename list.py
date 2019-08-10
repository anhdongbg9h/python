# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 23:51:22 2019

@author: haido
"""

empty_list=[]
empty_list.append(5)
empty_list[0]=23626

my_list=[0,1,2,3,4,5,6,7,8,9]
my_list[0]=13

mixed_list=[True,'hai_dong',5,4.3]

mixed_list.insert(0,'nguyen')

del mixed_list[1:3]

#total_list.remove('nguyen')

my_list.clear()
my_list.append(56)
total_list=my_list+mixed_list
#total_list.remove('nguyen')

my_list.pop(0)
print(empty_list)
print(my_list)
print(mixed_list)


print(total_list)