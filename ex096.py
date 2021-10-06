#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created on Wed Oct  6 10:25:35 2021
    @author: luciano
"""

def área(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg} x {comp} é de {a}m²')
    
    
print('-'*20)
print('Controle de terrenos')
print('-'*20)

l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))

área(l,c)