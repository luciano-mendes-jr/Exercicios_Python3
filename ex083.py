#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created on Sat Sep 18 10:31:35 2021
    @author: luciano
"""
expr = str(input('Digite a expressão: '))
pilha = []

for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            
if len(pilha) == 0:
    print('Sua expressão está válida !')
else:
    print('Sua expressão está errada !')
    