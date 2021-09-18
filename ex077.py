#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created on Wed Sep 15 12:08:58 2021
    @author: luciano
"""
palavras = ('Lapis', 'Borraca', 'Caderno', 'Estojo',  'Transferidor',
            'Compasso', 'Mochila', 'Canetas', 'Livro', 'Palavra',
            'Linhas', 'Pose', 'Faces', 'Brasileiro', 'mangas' ,'Capacho',
            'Acusado', 'Esquecendo', 'Notas' ,'Conflito','Abajuor')

vogais = 'aeiou'
s      = 0
total  = 0 

for p in palavras:
    print(f'\n Na palavra {p.upper()} --- temos: ', end = '')
    s = 0
    for l in p:
        if l.lower() in vogais:
            print(l, end = ' ')
            s += 1
    print(f' totalizando {s} vogais')
    total += s
    
print(f'Total de {total} vogais em {len(palavras)}. ')
print(f'Média {total/len(palavras)} vogais por palavra.')