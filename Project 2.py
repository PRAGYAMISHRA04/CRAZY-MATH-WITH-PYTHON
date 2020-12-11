# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 02:27:23 2020

@author: pragy
"""

def listing(l):
    A=""
    for i in range(len(l)-1):
        A+=l[i]+' , '
    A+='and '
    A+=l[-1]
    print(A)
listing(['apples','bananas','carrots','pizzas'])
    