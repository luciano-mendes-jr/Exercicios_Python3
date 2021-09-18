#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 19:00:35 2021

@author: luciano
"""
from random import choice 

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: ')) 

alunos = [n1, n2, n3, n4]

escolhido = choice(alunos)

print('O aluno escolhido foi: {}'.format(escolhido)) 



