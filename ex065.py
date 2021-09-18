#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created on Thu Sep  9 10:10:38 2021
    @author: luciano
"""

resp = ''
s = k = m = 0
maior = menor = 0
while resp in 'Ss':
    n = int(input('Digite um número: '))
    s += n
    k += 1
    resp = str(input('Quer continuar ? [S/N]: ')).upper().strip()[0]
    if k == 1:
        maior = menor = n 
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n 
            
m = s/k  
print('Você digitou {} números e a média foi {}.'.format(k,m))
print('O maior valor foi {} e o menor foi {}.'.format(maior,menor))
