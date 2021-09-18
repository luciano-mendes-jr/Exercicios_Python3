#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 17:02:20 2020
@author: luciano
"""
s = float(input('Qual é o salario do fucionario ? R$:'))

print("Um fucionario que ganhava R$:{:.2f}, com aumento de 15%, passa a ganhar R$:{:.2f}".format(s,s+(s*15/100)))
