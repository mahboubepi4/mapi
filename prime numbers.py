# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 14:35:36 2022

@author: Mahboobeh
Prime numbers
"""
for i in range(2,1000):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
            print(i, end = " - ")
    
