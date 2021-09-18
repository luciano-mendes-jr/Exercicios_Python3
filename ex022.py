#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 13:20:24 2021

@author: luciano
"""

nome = str(input("Entre com seu nome completo: ")).strip() 
print('Analisando seu nome ...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras.'.format(len(nome.split()[0])))

