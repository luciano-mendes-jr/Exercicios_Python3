#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 20:41:35 2021

@author: luciano
"""

velocidade = float(input('Qual é a velocidade atual do carro ? '))

if velocidade > 80:
    multa = (velocidade - 80)*7 
    print('MULTADO ! Você excedeu o limite permitido de 80km/h.')
    print('Você deve pagar uma multa de R$ {:.2f}.'.format(multa))
    
print('Tenha um bom dia ! Dirija com segurança !')