#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 16:37:11 2020
@author: luciano
"""

l = float(input('Digite a largura da parede: '))
h = float(input('Digite a altura da parede: '))

print('Sua parede tem dimensão de {}x{} e sua área é de {}m²'.format(l,h,l*h))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format((l*h)/2))