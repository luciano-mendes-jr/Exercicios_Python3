#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================
||     Created on Thu Sep 16 09:13:50 2021 ||
||     @author: luciano                    ||
=============================================
"""

lista = [] 

for i in range(0, 5):
    n = int(input('Digite um valor: ') )
    if i == 0 or n > lista[-1]:
        lista.append(n)
        print('Adcionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adcionado na pos {pos} da lista.')
                break 
            pos += 1
        
print('-=' * 30)

print(f'Os valores digitados em ordem foram {lista}')