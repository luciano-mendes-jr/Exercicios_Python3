#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created on Thu Nov  4 14:44:32 2021
    @author: luciano
"""
def notas(* n , sit = False):
    """
    Parameters
    ----------
    * n : lista
        DESCRIPTION: Uma ou mais notas dos alunos (aceita várias).
    sit : bool, optional
        DESCRIPTION: indica se deve ou não adicionar a situação do aluno 

    Returns
    -------
    r : dict
        DESCRIPTION: Dicionário com várias informações sobre a  situação do aluno
    """
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n)/len(n)
    if sit:
        if r['Média'] >= 7:
            r['Situação'] = 'BOA'
        elif r['Média'] >= 5:
            r['Situação'] = 'RAZOÁVEL'
        else:
             r['Situação'] = 'RUIM'
            
    return r 
    

resp = notas(5.5, 2.5, 8.5, sit = True)
print(resp)