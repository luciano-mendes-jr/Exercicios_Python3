#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 20:16:28 2021

@author: luciano
"""
from datetime import date 

ano = int(input('Ano de nascimento: '))
atual = date.today().year 
idade = atual - ano 

print("O atleta tem {} anos.".format(idade))
if idade <= 9:
    print("Classificação: MIRIM")
elif 9 < idade <= 14: 
    print("Classificação: INFANTIL")
elif 14 < idade <= 19: 
    print("Classificação: JÚNIOR")
elif 19 < idade <= 25: 
    print("Classificação: SÊNIOR")
elif idade > 25:
    print("Classificação: MASTER")
    