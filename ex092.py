#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created on Sat Sep 25 17:28:11 2021
    @author: luciano
"""
from datetime import datetime 

dados = {}

dados['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['Idade'] = datetime.now().year - nasc
dados['CTPS']  = int(input('Carteira de Trabalho (0 não tem): '))

if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano de Contratação: '))
    dados['Salário'] = float(input('Salário: R$ '))
    dados['Aposentadoria'] = dados['Idade'] + ((dados['Contratação'] + 35) -  datetime.now().year)

print('-=' * 20)

for k, v in dados.items():
    print(f' >> {k}: {v}')

