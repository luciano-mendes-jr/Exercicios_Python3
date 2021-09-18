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
m = 10
T = 0
print() 
while m != 0:
    T = T + m
    while k <= T:
        print('{} ↦ '.format(t), end = '')
        t += r
        k += 1
    print('PAUSA')
    m = int(input('Qunatos termos você quer mostrar a mais ? '))

print('Progressão finalizada com {} termos mostrados.'.format(T))