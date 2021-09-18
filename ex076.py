#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 12:08:58 2021

@author: luciano
"""

listagem = ('Lapis',   1.75,
            'Borraca', 2.00,
            'Caderno', 15.9,
            'Estojo',  25.0,
            'Transferidor', 4.2,
            'Compasso',9.99,
            'Mochila', 120.32,
            'Canetas',22.30,  
            'Livro', 34.9)

print('_' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('_' * 40)
for i in range(0,len(listagem)):
    if i % 2 == 0:    
        print(f'{listagem[i]:.<30}', end = '')
    else:
        print(f'R${listagem[i]:>7.2f}')
print('-' * 40)