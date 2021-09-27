#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created on Wed Sep 22 13:18:28 2021
    @author: luciano
"""

aluno = {}

aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] >= 7:
    aluno['Situação']  = 'Aprovado'
elif  5 <= aluno['Média'] < 7:
    aluno['Situação'] = 'Recuperação'
else: 
     aluno['Situação'] = 'Reprovado'
print('-'*20)  
for k, v in aluno.items():
    print(f'{k}:{v}')