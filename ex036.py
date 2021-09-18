#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Created on Sat Aug  7 21:04:01 2021
    @author: luciano
"""

vc = float(input('Valor da Casa: R$ '))

scp = float(input('Salario do Comprador: R$ '))

qaf = int(input('Quantos anos de Financiamento ? '))

vp = vc/(qaf*12)

print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}.'.format(vc,qaf, vp))

if vp >= scp*0.3:
    print('Emprestimo NEGADO')
else:
    print('Emprestimo CONCEDIDO')
