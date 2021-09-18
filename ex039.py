#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 13:16:09 2021

@author: luciano
"""
from datetime import date 

ano = int(input('Ano de nascimento: '))
atual = date.today().year 
idade = atual - ano 

print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, atual))

if idade == 18:
    print('Você tem que se alistar imediatamente.')
elif idade > 18:
    print('Você já deveria ter se alistado há {} anos.'.format(idade - 18))
    print('Seu alistamento foi em {}.'.format(ano + 18))
else:
    print('Ainda faltam {} anos para seu alistamento.'.format(18 - idade))
    print('Seu alistamento será em {}.'.format(ano + 18))
 