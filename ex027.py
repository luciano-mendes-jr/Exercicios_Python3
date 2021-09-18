#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 18:38:38 2021
@author: luciano
"""

nome = str(input("Qual é seu nome completo ? ")).strip().split()
print('Muito prazer em te conhecer !')
print('Seu primeiro nome é {}.'.format(nome[0])) 
print('Seu ultimo nome é {}.'.format(nome[len(nome)-1])) 