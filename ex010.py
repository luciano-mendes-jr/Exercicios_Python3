#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 16:22:53 2020
@author: luciano
"""


din = float(input('Quanto dinheiro você tem na carteira ? R$: '))
print('Com R$:{:.2f} você pode comprar US$:{:.2f}'.format(din,din/3.27))