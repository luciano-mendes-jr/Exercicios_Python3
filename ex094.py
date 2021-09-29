#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created on Wed Sep 29 13:17:53 2021
    @author: luciano
"""
pessoa = {}
grupo = []
soma = media = 0.0
while True:  
    pessoa.clear() 
    pessoa['nome'] = str(input('Nome: ')).capitalize() 
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO ! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma +=  pessoa['idade']
    grupo.append(pessoa.copy())
    while True:    
        resp = str(input('Quer continuar ? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO ! Por favor, digite apenas S ou N.') 
    if resp == 'N':
        break
print(f'Ao todo temos {len(grupo)} pessoas cadastradas.') 
media = soma/len(grupo)
print(f'A média de idade é de {media:5.2f} anos')
print(f'As mulheres cadastradas foram: ', end = '')
for p in grupo:
    if p['sexo'] in 'F':
        print(f'{p["nome"]}', end = ' ')
print()
print('Pessoas que estão com a idade acima da média: ', end = '')
for p in grupo:
    if p['idade'] >= media:
       print('    ', end = '')
       for k, v in p.items():    
           print(f'{k} = {v}; ', end = ' ')
       print()
        
    
    
    