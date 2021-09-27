#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created on Sat Sep 25 17:28:10 2021
    @author: luciano
"""
from random import randint 
from time import sleep
from operator import itemgetter
 
ranking = []
jogo = {'jogador_1': randint(1,6),
        'jogador_2': randint(1,6),
        'jogador_3': randint(1,6),
        'jogador_4': randint(1,6)}

print('Valores sorteados')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
    
ranking = sorted(jogo.items(), key = itemgetter(1), reverse = True)
print('-='*14)
print('== RANKING DOS JOGADORES ==')
print('-='*14)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)