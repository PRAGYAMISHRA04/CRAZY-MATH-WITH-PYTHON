# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 21:22:03 2020

@author: pragy
"""

L='58394934734896573243845758971234567891327844579895895588545884738572'
L=list(map(int,L))
G={}
i=0
while i<len(L)-1:
    if L[i+1]==L[i]+1:
        c=0
        A=[]
        while L[i+1]==L[i]+1 and i<len(L):
            c+=1
            A.append(L[i])
            i+=1
        G[c]=A
        del A
    i+=1
A=[]
for key in G.keys():
           A.append(key)
print(G[max(A)])
