#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sun Dec 27 15:21:52 2020
@author: luciano
"""
Qd = int(input('Quantidade de dias alugado: '))
kmr = float(input('Quantidade de Km rodados: '))
va = 60*Qd + kmr*0.15
print('O total a pagar é de R$:{}'.format(va))