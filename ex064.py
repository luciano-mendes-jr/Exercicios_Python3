#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created on Thu Sep  9 10:10:19 2021
    @author: luciano
"""
n = k = s = 0
n = int(input('Digite um número [999 para parar]: '))
while n!=999:
    k += 1
    s += n 
    n = int(input('Digite um número [999 para parar]: '))
    
print('Você digitou {} números e a soma entre eles foi {}'.format(k,s))
