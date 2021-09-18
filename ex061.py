#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created on Thu Sep  9 08:46:43 2021
    @author: luciano
"""
print('-='*10)
print('    Gerador de PA')
print('-='*10)

pr = int(input('Primeiro termo: '))
r  = int(input('Razão da PA: '))

t = pr 
k = 1 
print()
while k <= 10:
    print('{} ↦ '.format(t), end = '')
    t += r
    k += 1
print('FIM')