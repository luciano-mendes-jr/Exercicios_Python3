#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created on Tue Sep 21 10:53:38 2021
    @author: luciano
"""
num   = [[],[]] 
valor = 0 

for i in range(1, 8): 
    valor = int(input(f'Digite {i}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)

num[0].sort()
num[1].sort()
print(f'Os valores pares   digitados foram {num[0]}')        
print(f'Os valores impares digitados foram {num[1]}')   