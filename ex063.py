#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created on Thu Sep  9 08:55:30 2021
    @author: luciano
"""
print('-='*8)
print('    FIBONACCI')
print('-='*8)

n = int(input('Quantos termos você quer mostrar ? '))

t1 = 0
t2 = 1
t3 = 0
k  = 3

print('{} ↦ {}'.format(t1, t2), end = '')

while k <= n:
    t3 = t1 + t2 
    print(' ↦ {}'.format(t3), end = '')
    t1 = t2 
    t2 = t3 
    k += 1

print(' ↦ FIM')
