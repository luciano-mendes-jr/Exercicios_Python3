#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Created on Wed Oct  6 10:35:40 2021
    @author: luciano
"""

def escreve(msg):
    tam = len(msg) + 4
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)
    
    
frase = str(input('Qual frase você quer escrever ? : '))    
escreve(frase)