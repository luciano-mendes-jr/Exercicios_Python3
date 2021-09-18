#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 10:41:42 2021

@author: luciano
"""


while True:
    n = int(input('Quer a tabuada de qual valor ? '))
    if n < 0:
        break
    print('-'*20)
    for i in range(1, 11):
        print(f'{n} X {i} = {n*i}')    
    
    print('-'*20)
print('TABUADA ENCERRADA. Volte sempre !')
