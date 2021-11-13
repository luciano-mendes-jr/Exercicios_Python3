#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created on Wed Nov  3 11:25:43 2021
    @author: luciano
"""

def ficha(jog = '<desconhecido>', gol = 0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')
    
n = str(input('Nome do jogador: '))
g = str(input('Número de Gols: '))

if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol = g)
else:
    ficha(n, g)