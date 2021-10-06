#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Created on Wed Sep 29 13:18:04 2021
    @author: luciano
"""
jogador  = {}
partidas = []
time     = []

while True:    
    jogador['nome'] = str(input('Nome do Jogador: ')).capitalize()
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou ? '))
    partidas.clear() 
    for c in range(0, tot):
        partidas.append(int(input(f'   Quantos gols na partida {c} ? ')))
    jogador['gols'] = partidas[:]   
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar ? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO ! Responda apenas S ou N')
    if resp == 'N':
        break
print('-' * 40)   
print('cod', end = ' ')
for i in jogador.keys():
    print(f'{i:<15}', end = '')
print()
print('-' * 40)  
for k, v in enumerate(time):
    print(f'{k:>3} ', end = '')
    for d in v.values():
        print(f'{str(d):<15}', end = '')
    print()
print('-' * 40)
while True:
    buscar = int(input('Mostrar dados de qual jogador ? (999 para parar): '))
    if buscar == 999:
        break 
    if buscar >= len(time):
        print(f'ERRO! Não existe jogador com código {buscar}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[buscar]["nome"]}:')
        for i, g in enumerate(time[buscar]['gols']):
            print(f'   No jogo {i+1} fez {g} gols')
print('-' * 40)

              