#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 19:11:31 2021

@author: luciano
"""

from random import shuffle  

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: ')) 

alunos = [n1, n2, n3, n4]
shuffle(alunos)
print('A ordem de apresentação é: ')

print(alunos) 