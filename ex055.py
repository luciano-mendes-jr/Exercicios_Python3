#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 14:54:00 2021

@author: luciano
"""

for p in range(1,6):
    peso = float(input('Peso da {}ª pessoa: '.format(p)))
    
    if p == 1:
        maior = peso
        menor = peso 
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso 
            
print('O maior peso lido foi {}kg'.format(maior))
print('O menor peso lido foi {}kg'.format(menor))