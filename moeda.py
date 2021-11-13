#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    MODULO DO EXERCICIO 107
"""

def aumentar(preço, taxa):
    res =  preço + (preço * taxa/100.0)
    return res


def diminuir(preço, taxa):
    res =  preço - (preço * taxa/100.0)
    return res


def dobro(preço):
    res = preço * 2
    return res 


def metade(preço):
    res = 0.5 * preço 
    return res 