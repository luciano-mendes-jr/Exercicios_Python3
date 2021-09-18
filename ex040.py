#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created on Mon Aug  9 13:48:02 2021
    @author: luciano
"""
nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))

media = 0.5*(nota1 + nota2)

if media < 5:
    print('Você foi REPROVADO..')
elif  media >= 5 and media < 7 :
    print('Você está em RECUPERAÇÃO')
    print(media)
else:
    print('Parabéns você está  APROVADO.')
    print(media)