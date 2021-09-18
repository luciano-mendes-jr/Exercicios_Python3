#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 15:03:37 2021

@author: luciano
"""
SI = 0
MIH = 0
nomev = ''
Tm20 = 0
for p in range(1, 5):
    print('\n ----- {}ª PESSOA ----'.format(p))
    nome  = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo  = str(input('Sexo [M/F]: ')).strip()
    SI +=  idade 
    
    if p == 1 and sexo in 'Mn':
        MIH = idade 
        nomev = nome 
    if sexo in 'Mn' and idade > MIH:
        MIH = idade 
        nomev = nome
    if sexo in 'Ff' and idade < 20:
        Tm20 += 1
    
print('A média de idade do grupo é de {} anos.'.format(SI/4))
print('O homem mais velho tem {} anos e se chama {}.'.format(MIH,nomev))
print('Ao todos são {} mulheres com menos de 20 anos.'.format(Tm20))