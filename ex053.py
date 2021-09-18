#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 12:41:52 2021

@author: luciano
"""

frase = str(input('Digite uma frase: ')).strip().upper() 
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for k in range(len(junto) - 1, -1, -1):
    inverso += junto[k]
    
if(inverso == junto):
    print('Temos um palíndromo !')
else:
    print('Não temos um palíndromo !')
        