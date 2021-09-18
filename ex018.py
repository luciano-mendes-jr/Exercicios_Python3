#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 17:48:26 2021
@author: luciano
"""
from math import sin, cos, tan, radians 

ang = float(input('Digite o ângulo que você deseja: '))

rad = radians(ang)

print('O ângulo de {} tem SENO de: {:.2f}'.format(ang, sin(rad)))
print('O ângulo de {} tem COSSENO de: {:.2f}'.format(ang, cos(rad)))
print('O ângulo de {} tem TANGENTE de: {:.2f}'.format(ang, tan(rad)))
