# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 08:51:18 2016

@author: Bruno Dratcu
"""

import random
interacoes = 100000

opcoes = ["R$10,00", "R$10,00", "R$1M,00"]
vitorias = 0.0
derrotas = 0.0

for i in range(interacoes):
    n = random.randrange(0,3)

    escolhas = opcoes[n]
    
    if n == 0:
        vitorias += 1
        
    elif n == 1:
        vitorias += 1
        
    elif n == 2:
        derrotas += 1
        
    else:
        print("Ja era!")

t = (vitorias/interacoes) * 100
print("Vitorias: " + str(vitorias))
print("Derrotas: " + str(derrotas))
print("Porcentagem de vitorias (em %): " + str(t))