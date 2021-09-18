#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 13:53:05 2021

@author: luciano
"""

num = int(input("Informe um numero: "))

u = num // 1    % 10 #Calcula Unidade 
d = num // 10   % 10 #Calcula Dezena
c = num // 100  % 10 #Calcula Centena
m = num // 1000 % 10 #Calcula Milhar 
print('Analisando o numero {}.'.format(num))
print('Unidade: {}'.format(u))
print('Dezena:  {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar:  {}'.format(m))