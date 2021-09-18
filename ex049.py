#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created on Mon Aug 16 16:07:41 2021
    @author: luciano
"""

n = int(input('Digite um valor para ver sua tabuada: '))

for i in range(0, 11):
    print('{} x {} = {}'.format(n,i, n*i))
    