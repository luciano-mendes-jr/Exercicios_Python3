#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 08:45:57 2021

@author: luciano
"""

n = int(input('Digite um número para calcular o seu Fatorial: '))

print('Calculando {}! = '.format(n), end = '')
c = n 
f = 1
while(c > 0):
    print('{}'.format(c), end = '')
    print(' X ' if c > 1 else ' = ', end = '')
    f *= c
    c -= 1
print('{}'.format(f))