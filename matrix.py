# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 22:12:52 2019

@author: haido
"""

def matrix_multiplication(matrix1,matrix):
    matrix1_nrows=len(matrix1)
    matrix1_ncols=len(matrix1[0])
    
    matrix2_nrows=len(matrix2)
    matrix2_ncols=len(matrix2[0])
    
    result=[[0]*matrix2_ncols for i in range(matrix1_nrows)]
    for i in range(matrix1_nrows):
        for j in range(matrix2_ncols):
            for k in range(matrix1_ncols):
                result[i][j]+=matrix[i][k]*matrix[k][j]
    return result
matrix1=[[1,2,3],
         [4,5,6],
         [7,8,9]]

matrix2=[[1,1,2,1],
         [1,2,1,1],
         [1,1,1,2]]

result=matrix_multiplication(matrix1,matrix2)

print(result)
    