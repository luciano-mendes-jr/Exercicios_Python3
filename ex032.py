#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 21:50:49 2021

@author: luciano
"""

from datetime import date 

ano = int(input('Que ano você quer analisar ? Digite 0 para analisar o ano atual.'))

if ano == 0:
    ano = date.today().year 
if ano % 4 == 0 and ano %100 !=0 or ano %400 == 0:
    print('O ano {} é BISEXTO.'.format(ano))
else:
    print('O ano {} não é BISEXTO.'.format(ano))
    