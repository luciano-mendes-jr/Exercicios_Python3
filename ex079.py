#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created on Thu Sep 16 09:13:47 2021
    @author: luciano
"""

num = []
while True:
    n = int(input('Digite um valor: '))
    if n not in num:
        num.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado não vou adicionar ...')
    r = str(input('Quer continuar ? [S/N] ')).upper()[0]
    if r in 'N':
        break 
num.sort()
print(f'Os valores digitados foram: {num} ')

