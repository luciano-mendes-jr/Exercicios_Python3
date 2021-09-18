#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 18:20:20 2021

@author: luciano
"""

salario = float(input('Qual salario do funcionario ? R$: '))

if salario > 1250.0:
   aumento = salario + (salario * 0.10)
else: 
   aumento = salario + (salario * 0.15) 
   
print('Quem ganhava R${:.2f} para ganhar R${:.2f} agora.'.format(salario, aumento))

