#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 00:01:00 2021

@author: luciano
"""

num = int(input('Digite um número inteiro: '))
print(''' Escolha uma das bases para conversão
      [ 1 ] cpnverter para BINÁRIO
      [ 2 ] cpnverter para OCTAL
      [ 3 ] cpnverter para HEXADECIMAL''')

op = int(input('Digite a opção: '))

if op == 1:
    print('{} convertido para BINÁRIO é igual a {}.'.format(num, bin(num)[2:]))
elif op == 2:
    print('{} convertido para OCTAL é igual a {}.'.format(num, oct(num)[2:]))
elif op == 3:
    print('{} convertido para HEXADECIMAL é igual a {}.'.format(num, hex(num)[2:]))
else:
    print('DIGITE UMA OPÇÃO VALIDA !')