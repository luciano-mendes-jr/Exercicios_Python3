#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created on Thu Sep 16 09:13:47 2021
    @author: luciano
"""

num = []
mai = men = 0
print('+='*30)
for i in range(0, 5):
    num.append(int(input(f'Digite um valor para a Posição {i} :'))) 
    if i == 0:
        mai = men = num[i]
    else:
        if num[i] > mai:
            mai = num[i]
        if num[i] < men: 
            men = num[i]
print('+='*30)
print(f'Você digitou os valores {num}.')
print(f'O maior que você digitou foi {mai}, nas posições ', end = '')
for i, v in enumerate(num):
    if v == mai:
        print(f'{i}...', end = '')
print()       
print(f'O menor que você digitou foi {men}, nas posições ', end = '')
for i, v in enumerate(num):
    if v == men:
        print(f'{i}...', end = '')