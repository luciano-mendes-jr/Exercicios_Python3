#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created on Wed Oct  6 10:35:40 2021
    @author: luciano
"""
from time import sleep

def contador(i, f, p):
    if p < 0:
       p *= -1
    if p == 0:
       p = 1 
       
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)
    if i < f:
        cont = i 
        while cont <= f:
            print(f'{cont} ', end = '')
            sleep(0.5)
            cont += p
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end = '')
            sleep(0.5)
            cont -= p
    print('FIM!')
    
contador(1, 10, 1)  
contador(10, 0, 2) 

print('Agora é sua vez de personalizar a contagem')

ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: ')) 

contador(ini, fim, pas)