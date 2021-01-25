# -*- coding: utf-8 -*-
"""
Created on Mon May 18 05:40:14 2020

@author: pragy
"""

U=[];D=[];L=[];R=[];Diag=[]
mat=[]
PROD=[]
l=M.rstrip().split()
for i in range(len(l)):
    l[i]=int(l[i])    
for i in range(1,21):
    K=[]
    for j in range(20):
         K.append(l[j])
    l=l[20:]
    mat.append(K)
    del K
for i in mat:
     PROD.append(i)
for i in range(20):
    for j in range(0,17):      
          R.append(mat[i][j:j+4])
for i in R:
     PROD.append(i)       
for i in range(20):
     for j in range(20,3,-1):
                L.append(mat[i][j-4:j])   
for i in L:
     PROD.append(i)
for i in range(20):
     for j in range(17):
         d=[]
         for k in range(4):
             d.append(mat[j+k][i]) 
         D.append(d)
         del d
for i in D:
    PROD.append(i)
for i in range(20):
     for j in range(16,-1,-1):
         u=[]
         for k in range(3,-1,-1):
             u.append(mat[j+k][i]) 
         U.append(u)
         del u        
for i in U:
    PROD.append(i)
i=0;j=0;k=0;
Di=[]
while i<20:
    while j<20:
        Di=[];k=0;
        while k<4:
            if i==j:
                 Di.append(mat[i][j])
                 k+=1
            i+=1
            j+=1
        Diag.append(Di)
        del Di        
for i in Diag:
    PROD.append(i)             
def prod(H):
    return H[0]*H[1]*H[2]*H[3]
for i in range(len(PROD)):
    PROD[i]=prod(PROD[i])
print(max(PROD))    
             
             
             
             
