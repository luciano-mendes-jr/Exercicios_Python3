#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 20:00:45 2021

@author: luciano
"""

from random import randint 
from time import sleep 
n = randint(0, 5)
print('Pensei em um número...')
num = int(input('Qual número foi ? '))
print('PROCESSANDO...')
sleep(3)
if num == n:
    print('Parabéns, você ganhou !')
else:
    print('Ganhei! Eu pensei no número {} e não no {}.'.format(n,num))
