#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 19:15:53 2021

@author: luciano
"""
from random import randint 
from time import sleep 

itens = ('Pedra' , 'Papel',  'Tesoura')
computador = randint(0,2)

print('''Suas opções
[ 0 ] PEDRA
[ 1 ] PAPEL 
[ 2 ] TESOURA 
''')
 
jogador = int(input('Qual é a sua jogada: '))


print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
 


print('-='*12)
print('Computador jogou {}'.format(itens[computador]))
print('jogador jogou {}'.format(itens[jogador]))
print('-='*12)


if computador == 0:
    
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR GANHAR')
    elif jogador  == 2:
        print('COMPUTADOR GANHAR')
    else:
        print('ENTRADA INVALIDA')
        
elif computador == 1:
    
    if jogador == 0:
        print('COMPUTADOR GANHAR')
    elif jogador == 1:
        print('EMPATE')
    elif jogador  == 2:
        print('JOGADOR GANHAR')
    else:
        print('ENTRADA INVALIDA')
 
elif computador == 2:
     
    if jogador == 0:
         print('JOGADOR GANHAR')
    elif jogador == 1:
         print('COMPUTADOR GANHAR')
    elif jogador  == 2:
         print('EMPATE')
    else:
        print('ENTRADA INVALIDA')
    