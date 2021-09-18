#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 13:27:13 2021

@author: luciano
"""

from datetime import date 

atual = date.today().year 

nma = 0
nme = 0

for n in range(1,8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu: '.format(n))) 
    ida = atual - nasc  
    if ida >= 21:
        nma += 1
    else:
        nme +=1

print("Ao todo temos {} pessoas maiores de idade.".format(nma))
print("Ao todo temos {} pessoas menores de idade.".format(nme))