#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created on Tue Aug 17 13:08:49 2021
    @author: luciano
"""

n = int(input('Digite um numero inteiro: '))
k = 0
for i in range(1, n + 1):
    
    if n % i == 0:
        print('\033[m', end = ' ')
        k += 1
    else:
        print('\033[31m', end = ' ')
    print('{}'.format(i), end = ' ')

print('\n\033[mO número {} foi divisível {} vezes.'.format(n, k))

if k == 2:
    print('E por isso ele é PRIMO')
else:
    print('E por isso ele NÃO é PRIMO')
    