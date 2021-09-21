#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created on Tue Sep 21 10:53:38 2021
    @author: luciano
"""
matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

for i in range(0, 3):
  for j in range(0, 3):
      matriz[i][j] = int(input(f'Digite um valor para [{i}, {j}]: '))
print('-=' * 30)

for i in range(0, 3):
  for j in range(0, 3):
      print(f'[{matriz[i][j]:^5}]', end = '')
  print()
