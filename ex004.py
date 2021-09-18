#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 09:02:26 2020
@author: luciano
"""

a = input('Digite algo: ')
print('O tipo primitivo desse valor é: ', type(a))
print('So tem espaços ? ', a.isspace())
print('É um número ? ', a.isnumeric())
print('É alfabetico ? ', a.isalpha())
print('É alfanumérico ? ', a.isalnum())
print('Está em maiúsculas ? ', a.isupper())
print('Está e minusculas ? ', a.islower())
print('Está capitalizada ? ', a.istitle())


