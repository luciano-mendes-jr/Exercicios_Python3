#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 10:41:11 2021

@author: luciano
"""
S = 0
c = 0
while True: 
    n = int(input('Entre com um número [999 para parar]: '))
    if n == 999:
        break    
    S += n
    c += 1
print(f'A soma dos {c} valores é {S}.')