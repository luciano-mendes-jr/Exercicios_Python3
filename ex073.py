#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 18:49:32 2021

@author: luciano
"""

times = ('Atletico - MG', 'Palmeiras', 'Flamengo', 'Fortaleza','Bragantino'
         'Corinthians', 'Fluminense', 'Cuiabá', 'Internacional','Atletico - GO',
         'Athletico - PR', 'Ceará - SC', 'Santos','Juventude','Bahia','São Paulo',
         'América - MG', 'Grêmio', 'Sport Recife','Chapecoense')
print('-=' * 15)
print(f'Lista de times: {times}.')
print('-=' * 15)
print(f'Os 5 primeiros são: {times[0:6]}')
print('-=' * 15)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' * 15)
print(f'Times em orgem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O chapecoense está na {times.index("Chapecoense")}')