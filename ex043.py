#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created on Tue Aug 10 21:31:24 2021
    @author: luciano
"""

peso = float(input('Qual é seu peso ?  (Kg) '))
h = float(input('Qual é sua altura ? (m) '))
imc = peso/(h**2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))

if imc < 18.5:
    print('Você está ABAIXO DO PESO normal.')
elif 18.5 <= imc  < 25:
    print('Parabéns, você está na faiza de PESO NORMAL.')
elif 25 <= imc  < 30: 
    print('você está em SOBREPESO.')
elif 30 <= imc  < 40: 
    print('você está em OBESIDADE.')
else:
    print('você está em OBESIDADE MÓRBIDA, cuidado !!')
