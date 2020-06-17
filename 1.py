# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 21:12:35 2020

@author: PRAGYA
"""

from numpy import *
M=array([23, 46, 59, 34, 66, 19, 56, 9])
N=array([11,47,81,29,36,91,51,46,26,31,82,30])
c=0 
for i in M:
    for j in N:
        if i+j==90:
            c+=1
for i in M:
   for j in M:
        if i+j==90:
           c+=1
for i in N:
     for j in N:
        if i+j==90:
          c+=1
print(c)            
            
