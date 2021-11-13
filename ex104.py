#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created on Wed Nov  3 11:27:10 2021
    @author: luciano
"""
def leiaInt(msg):
    ok = False 
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido. \033[m')
        if ok:
            break
    return valor 


n = leiaInt('Digite um número: ')
print(f'você digitou o número {n}.')