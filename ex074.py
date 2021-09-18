#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created on Tue Sep 14 18:49:48 2021
    @author: luciano
"""

from random import randint 

numeros = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))

print('Os valores sorteados foram: ', end = '')

for n in numeros:
    print(f'{n}', end = ' ')

print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'\nO menor valor sorteado foi {min(numeros)}')