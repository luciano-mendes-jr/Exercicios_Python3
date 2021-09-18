#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 21:27:51 2021

@author: luciano
"""

d = float(input('Qual é a distancia em km da sua viagem ?: '))
print('Você está prestes a começar uma viagem de {:.1f}km'.format(d))
if d > 200:
    print('E o preço da sua passagem será R$ {:.2f}.'.format(d*0.45))
else:
    print('E o preço da sua passagem será R$ {:.2f}.'.format(d*0.5))
    