# -*- coding: utf-8 -*-
"""
Created on Thu May 14 23:44:51 2020

@author: pragy
"""
def fibb(N,summ,now_1,now_2):
              if now_2>=N : 
                  return summ
              else: 
                 if (now_1+now_2)%2==0:
                     summ+=now_1+now_2
                     return fibb(N,summ,now_2,now_1+now_2)
                 else:
                     return fibb(N,summ,now_2,now_1+now_2) 
print(fibb(4000000,0,1,1))  
                
                          
