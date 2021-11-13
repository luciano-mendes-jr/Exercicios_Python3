#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import moeda 

p = float(input('Digite o preço: R$ '))
tx = float(input('Digite a taxa: (%) '))
print(f'A metade de R${p} é R${moeda.metade(p):.2f}')
print(f'O dobro de  R${p} é R${moeda.dobro(p):.2f}')
print(f'Aumentando {tx:.2f}% em R${p:.2f}, temos R${moeda.aumentar(p,tx):.2f}')
print(f'Diminuindo {tx:.2f}% em R${p:.2f}, temos R${moeda.diminuir(p,tx):.2f}')