#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created on Mon Aug 16 15:59:26 2021
    @author: luciano
"""

s = 0
k = 0

for n in range(1, 501, 2):
    if(n % 3 == 0):
         s += n 
         k += 1
         
print('A soma de todos os {} valores solicitados é {}.'.format(k,s))
