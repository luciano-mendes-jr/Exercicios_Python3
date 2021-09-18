#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 13:38:23 2021

@author: luciano
"""

s1 = float(input('Primeiro Segmento: '))
s2 = float(input('Segundo  Segmento: '))
s3 = float(input('Terceiro Segmento: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos acima PODEM FORMAR um triângulo.')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo.')
    