#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created on Tue Aug 17 13:00:49 2021
    @author: luciano
"""

n = int(input('Primeiro termo: '))
r = int(input('Razão: '))

D = n + (10 - 1)*r

for i in range(n, D + r, r):
    print('{}'.format(i), end = ' - ')
print('ACABOU')
