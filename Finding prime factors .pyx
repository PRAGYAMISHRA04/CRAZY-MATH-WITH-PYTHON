# -*- coding: utf-8 -*-
"""
Created on Fri May 15 01:53:43 2020

@author: pragy
"""
def check_prime(n):
    i=2;c=0;
    while i<=n:
        if n%i==0:
            c+=1
            return False
        i+=1
    if c==0:
        return True
def fact(N):
    i=2
    while i<=N:
        if N%i==0:
            if bool(check_prime(N/i)):
                return N/i
            else:
                fact(N/i)
        i+=1  
N=int(input())
print(fact(N))
'''Prime dividing by  i=1 to N/2     '''  
  
