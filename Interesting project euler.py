# -*- coding: utf-8 -*-
"""
Created on Sat May 16 00:17:39 2020

@author: pragy
"""

'''2520 is the smallest number that can be divided by each of the numbers from 1 to 10 
   without any remainder.
   What is the smallest positive number that is evenly
   divisible by all of the numbers from 1 to 20?
    20 1 2 4 5 10 20
    19
    18 1 2 3 6 9 18
    17
    16 1 2 4 8 
    15 1 3 5 15
   14 1 2 7 14
   13 
   12 1 2 3 4 6 12
   11 
 
 '''
def divide(a,B):
    for k in range(len(B)):
        if B[k]%a==0:
            B[k]=int(B[k]/a)
    #print(B)        
    return B  
'''def check(b,C) :
    for k in C:
        if k%b==0:
            return True
    return False     
'''
import numpy as np
LCM=[]
L=np.arange(1,20,1)
P=[2,3,5,7,11,13,17,19]
for j in range(len(P)):
    for i in range(len(L)):
        if L[i]%P[j]==0 :
            L=divide(P[j],L)
            #print(L)
            LCM.append(P[j])
lcm=1
for l in LCM:
    lcm=lcm*l
print(lcm)    
            
    
         










    
