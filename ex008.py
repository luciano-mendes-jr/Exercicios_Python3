#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 15:53:42 2020
@author: luciano
"""

m = float(input('Um distancia em metros: '))
print('A medida de {}m corresponde a: '.format(m))
print('\n{}km'.format(m/1000))
print('\n{}hm'.format(m/100))
print('\n{}dam'.format(m/10))
print('\n{}dm'.format(10*m))
print('\n{}cm'.format(100*m)) 
print('\n{}mm'.format(1000*m))

