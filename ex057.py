#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Created on Sat Sep  4 12:39:09 2021
    @author: luciano
"""

sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]

while sexo not in 'MF':
    sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
    
print('Sexo {} registrado com sucesso.'.format(sexo))