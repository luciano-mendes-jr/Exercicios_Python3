#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created on Wed Sep  8 09:29:54 2021

    @author: luciano
"""
from time import sleep 

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
op = 0
while op != 5:     
    print('''    [ 1 ] Somar 
    [ 2 ] Multiplicar       
    [ 3 ] Maior 
    [ 4 ] Novos números 
    [ 5 ] Sair do programa''')
    op = int(input('>> Qual é sua opção? '))
    if op == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
    elif op == 2:
        mult = n1*n2
        print('O resultado de {} X {} é {}'.format(n1, n2, mult))
    elif op == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}.'.format(n1, n2, maior))
    elif op == 4:
        print('Informe os números novamente.')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif op == 5:
        print('Finalizando...') 
        sleep(2)
    else:
        print('Opção inválida. Tente novamente!')
    print('=-=' * 10)
    
print('Fim do programa ! Volte sempre!')