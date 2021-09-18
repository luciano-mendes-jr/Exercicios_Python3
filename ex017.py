#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 14:31:26 2020

@author: luciano
"""
from math import hypot

cop = float(input('Digite o comprimento do cateto oposto: '))
cad = float(input('Digite o comprimento do cateto adjacente: '))

hip = hypot(cop, cad)

print('A hipotenusa vale: {:.2f}'.format(hip))

