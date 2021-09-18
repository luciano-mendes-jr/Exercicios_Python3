#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created on Tue Sep 14 18:49:08 2021
    @author: luciano
"""

cont = ('zero',  'um', 'dois', 'três', 'quatro',
       'cinco', 'seis', 'sete', 'oito', 'nove',
         'dez', 'onze', 'doze', 'treze','quatorze', 
      'quinze', 'dezesseis', 'dezessete', 'dezoito',
    'dezenove','vinte') 


while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0<= num <=20: 
        break 
    print('Tente novamente !!')

print(f'você digitou o número {cont[num]}.')