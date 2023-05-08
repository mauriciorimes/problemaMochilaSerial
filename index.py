import time as t
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

#writefile mochila_serial.py
# Importando as bibliotecas
import random
import sys

random.seed(1)

# Definições
CAP_MOC = int(sys.argv[1])   # 30
TAM_LOJA = int(sys.argv[2])  # 5
QTD_PROD = int(sys.argv[3])  # 3
MAX_PRECO = int(sys.argv[4]) #20
MAX_VOL = int(sys.argv[5])   #10

# Gerador de combinações
def conv_base(num, base, exp):
    valor = num
    saida=[]
    while valor > 0:
        saida.append(valor % base)
        valor = valor // base
    while len(saida) < exp:
        saida.append(0)
    saida = [saida[len(saida)-i-1] for i in range(len(saida))] 
    return saida

#Gerando o intervalo das combinações
def gera_inter(base, exp, inicio, fim):
    saida=[]
    for i in range(inicio, fim):
        saida.append(conv_base(i, base, exp))
    return(saida)

#Gerando a loja
def gera_loja(tam, max_preco, max_vol):
    loja=[]
    for i in range(tam):
        loja.append((random.randint(1, max_preco), random.randint(1, max_vol)))
    return loja

# Cálculo do custo e volume da combinação
def custo_vol(loja, comb):
    custo = 0
    vol = 0
    for i in range(len(loja)):
        custo += loja[i][0] * comb[i]
        vol += loja[i][1] * comb[i]
    return (custo, vol)

#gerando a loja
loja = gera_loja(TAM_LOJA, MAX_PRECO, MAX_VOL)
#print(loja) #debug

comb = gera_inter(QTD_PROD, TAM_LOJA, 0, QTD_PROD**TAM_LOJA)
#print(comb)

max = (0, 0)
max_comb = []
for teste in comb:
    resp = custo_vol(loja, teste)
    if resp[0] >= max[0] and resp[1] <= CAP_MOC:
        max = resp
        max_comb = teste     
        
print(loja)
print(max_comb)
print(max)

# Teste CAP_MOC, TAM_LOJA, QTD_PROD, MAX_PRECO, MAX_VOL
#!python mochila_serial.py 30 5 11 20 10

CAP_MOC   = 30    # Capacidade da Mochila
TAM_LOJA  = 12    # Tamanho da Loja (Variedade de Produtos)
QTD_PROD  = 3     # Quantidade limitada de cada produto
MAX_PRECO = 20    # Maior preço possível
MAX_VOL   = 10    # Maior volume possível
