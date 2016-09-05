# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 08:51:18 2016

@author: Bruno Dratcu
"""

import random

#iterations = int(raw_input("How many iterations? >> "))
interacoes = 100000

opcoes = ["R$10,00", "R$10,00", "R$1M,00"]
vitorias = 0.0
derrotas = 0.0

for i in range(interacoes):
    n = random.randrange(0,3)

    escolhas = opcoes[n]
    
    if n == 0:
#        print("Escolheu a porta 1")
#        print("Abriu a porta 2")
#        print("Mudou para a porta 3")
        vitorias += 1
#        print("Na porta estava" + opcoes[2] + "\n")
        
    elif n == 1:
#        print("Escolheu a porta 2")
#        print("Abriu a porta 1")
#        print("Mudou para a porta 3")
        vitorias += 1
#        print("Na porta estava " + opcoes[2] + "\n")
        
    elif n == 2:
#        print("Escolheu a porta 3")
#        print("Abriu a porta 2")
#        print("Mudou para a porta 1")
        derrotas += 1
#        print("Na porta estava " + opcoes[0] + "\n")
        
    else:
        print("Ja era!")

t = (vitorias/interacoes) * 100
print("Vitorias: " + str(vitorias))
print("Derrotas: " + str(derrotas))
print("Porcentagem de vitorias (em %): " + str(t))