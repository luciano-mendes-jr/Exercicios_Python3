#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 16:25:12 2021

@author: luciano
"""
s = 0
for n in range(1,7):
    k = int(input('Digite um valor: '))
    if( k % 2 == 0):
        s += k
        
print('A soma de todos os valores pares é {}.'.format(s))
