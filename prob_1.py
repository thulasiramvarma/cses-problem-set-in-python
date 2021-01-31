#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 11:35:21 2020

@author: sai4
"""

a=int(input())


print(int(a))

while a!=1:  
    if a==1:
        break
        temp = a
    elif a%2==0:
        temp=a/2
    else:
        temp=a*3+1
    a=temp
    print(int(temp))

    

