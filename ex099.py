#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 11:36:42 2021

@author: luciano
"""
from time import sleep 

def maior(*num): 
    cont = maior = 0
    print('=-' * 30)
    print('Analisando os valores passados... ')
    for valor in num:
        print(f'{valor} ', end = '')
        sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor      
        cont += 1
    print()    
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')

    
maior(2,9,7,1,6)
maior(10, 11, 13, 7, -0)
