# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 01:53:41 2020

@author: pragy
"""

def collatz(n):
     if n==1:
        print("Haha !! The End ")
     elif n%2==0:
         print(n//2)
         return collatz(n//2)
     else:
         print(3*n+1)
         return collatz(3*n+1)
N=int(input("LOLOLOL !!!!!! Give number man "))
collatz(N)     
     