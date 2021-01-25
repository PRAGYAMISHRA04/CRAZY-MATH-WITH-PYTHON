# -*- coding: utf-8 -*-
"""
Created on Thu May 14 23:37:42 2020

@author: pragy
"""

def res_1(N):
    summ=0
    for i in range(1,N):
        if i%3==0 or i%5==0:
            summ+=i
    return summ
res_1(10000)        
