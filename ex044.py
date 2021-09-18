#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 19:15:37 2021

@author: luciano
"""

print('{:=^40}'.format(' LOJAS LSMJ '))

valor = float(input("Preço das compras: R$  ")) 

print(''' FORMAS DE PAGAMENTO 
      [ 1 ] à vista dinheiro/cheque 
      [ 2 ] à vista cartão 
      [ 3 ] 2x no cartão 
      [ 4 ] 3x ou mais no cartão''')

op = int(input("Qual é a opção ?  ")) 

if   op == 1:
    total  = valor - (valor*0.1)
elif op == 2:
    total  = valor - (valor*0.05)
elif op == 3:
    total = valor 
    par = total/2 
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(par))
elif op == 4:
    total = valor + (valor*0.2)
    par = int(input('Quantas parcelas ? '))
    final = total/par 
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(par, final))
else:
    total = 0 
    print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE')
    
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor, total))