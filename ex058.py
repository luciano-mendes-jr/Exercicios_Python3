#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created on Wed Sep  8 09:17:22 2021
    @author: luciano
"""
from random import randint 

computador = randint(0,10)

print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi ?')

acertou = False 
np = 0

while not acertou:
    jogador = int(input('Qual seu palpite ? '))
    np += 1 
    if jogador == computador:
        acertou = True 
    else:
        if jogador < computador:
            print('Mais... tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
            
print('Acertou com {} tentativas. Parabéns !!'.format(np))