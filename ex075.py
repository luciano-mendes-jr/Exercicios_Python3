#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 12:08:57 2021

@author: luciano
"""


num = (int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')))

print(f'Você digitou os valores {num}.')
print(f'O valor 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3) + 1}ª posição.')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição.')
    
print('Os valores pares digitados foram:  ', end ='')

for n in num:
    if n % 2 == 0:
        print(n, end = ',')