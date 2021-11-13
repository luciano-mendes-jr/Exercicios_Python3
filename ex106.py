#!/usr/bin/env python3
# -*- coding: utf-8 -*-
c = ('\033[m', 
     '\033[0;30;41m', 
     '\033[0;30;42m',
     '\033[0;30;43m',
     '\033[0;30;44m',
     '\033[0;30;45m',
     '\033[0;30m')


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'',4)
    print(c[4], end = '')
    help(com)
    print(c[0], end = '')

def titulo(msg, cor = 0):
    tam = len(msg)
    print(c[cor], end = '')
    print('-' * (tam+2))
    print(f' {msg}')
    print('-' * (tam+2))
    print(c[0], end = '')
    

#programa principal 
comando = ''

while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input("Função ou biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)

titulo('ATÉ LOGO', 1)