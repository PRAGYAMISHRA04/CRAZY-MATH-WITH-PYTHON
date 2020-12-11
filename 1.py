# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 09:07:09 2020

@author: pragy
"""
def n(a):
    for i in range(10):
        print(int(a+2*i))
def check(a):
   a=float(a)
   if a.is_integer() and a>0:
        if a%2==0:
            print('Even')
        else:
            print('Odd')
        n(a)
   else:
       print("Enter a positive integer")
if '__name__' == '__main__ ':
    a=int(input('\n Enter the digit '))
    check(a)
    n(a)