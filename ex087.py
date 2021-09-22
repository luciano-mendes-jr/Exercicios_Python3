#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 13:17:46 2021

@author: luciano
"""

matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

sop = scol = 0

for i in range(0, 3):
  for j in range(0, 3):
      matriz[i][j] = int(input(f'Digite um valor para [{i}, {j}]: '))
print('-=' * 30)
for i in range(0, 3):
  for j in range(0, 3):
      print(f'[{matriz[i][j]:^5}]', end = '')
      if matriz[i][j] % 2 == 0:
         sop += matriz[i][j]
          
  scol += matriz[i][2]     
  print()
print('-=' * 30)

print(f'A soma dos valores pares é {sop}')
print(f'A soma dos valores da terceira coluna é {scol}')
print(f'O maior valor da segunda linha é {max(matriz[1][:])}')
