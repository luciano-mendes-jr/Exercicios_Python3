#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 13:17:47 2021

@author: luciano
"""
from random import randint 
from time import sleep 

lista = []
jogos = []
n = 0
k = 0
print('-' * 30)
print('      JOGA NA MEGA SENA      ')
print('-' * 30)

m = int(input('Quantos jogos você quer que eu sorteie ?  '))

while k < m:
    n = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            n+= 1
        if n >= 6:
            break 
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    k += 1 
    
print('-=' * 3, f' SORTEANDO {m} JOGOS', '-=' * 3) 

for i, j in enumerate(jogos):
    print(f'Jogo {i + 1}: {j}')
    sleep(0.85)

print('>>' * 3, 'BOA SORTE ', '<<' * 3)    