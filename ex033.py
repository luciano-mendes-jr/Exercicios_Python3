#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 17:48:09 2021

@author: luciano
"""

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo  número: '))
n3 = int(input('Digite o terceiro número: '))

menor = n1 
maior = n1

if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3 
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3 
    
print('O menor número é {}'.format(menor))
print('O maior número é {}'.format(maior))