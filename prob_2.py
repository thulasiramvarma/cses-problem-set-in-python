#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 12:22:01 2020

@author: sai
"""

x=int(input())
a = [int(x) for x in input().split()]
x_sum=0
a_sum=0
for i in range (1,x+1):
    x_sum=x_sum+i

for i in range (len(a)):
    a_sum=a_sum+a[i]

output=x_sum-a_sum
print(output)
