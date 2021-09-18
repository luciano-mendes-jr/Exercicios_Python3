#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created on Sun Sep 12 10:44:53 2021
    @author: luciano
"""
print('='*30)
print('{:^30}'.format('BANCO LULU'))
print('='*30)

valor = int(input('Que valor você quer sacar ? R$ '))

total = valor 
ced = 50
n = 0
while True:
    if total >= ced:
        total -= ced 
        n += 1
    else:
        if n > 0:
            print(f'Total de {n} cédulas de R$ {ced}.')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10 
        elif ced == 10:
            ced = 1
        n = 0
        if total == 0:
            break
print('='*45)
print('Volte sempre ao BANCO LULU! Tenha um bom dia !')
print('='*45)
