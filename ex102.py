#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created on Wed Nov  3 10:51:43 2021
    @author: luciano
"""
def fatorial(n, show = False):
    """
    Parameters
    ----------
    n : int
        DESCRIPTION: Número a ser calculado.
    show : bool (opcional) 
        DESCRIPTION: Mostrar ou não a conta.

    Returns
    -------
    f : int
        DESCRIPTION: O valor do fatorial  do número n

    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(f'{c}', end = '')
            if c > 1:
                print(' x ', end = '')
            else:
                print(' = ', end = '')
        f *= c
    return f


print(fatorial(10, show = True))