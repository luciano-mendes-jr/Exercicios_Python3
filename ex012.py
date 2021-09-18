#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 16:48:15 2020
@author: luciano
"""

valor = float(input('Qual é o preço do produto? R$:'))
print('''O produto que custava R$:{:.2f}, na promoção com o desconto de 5% vai custar R$:{:.2f}.'''
         .format(valor,(valor-valor*(5/100)))
     )

