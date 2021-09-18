#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 10:31:34 2021

@author: luciano
"""

num     = []
pares   = []
impares = []

while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar ? [S/N] '))
    if resp in 'Nn':
        break 

for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)

print(f'A lista completa é {num}.')
print(f'A lista de pares é {pares}.')
print(f'A lista de pares é {impares}.')