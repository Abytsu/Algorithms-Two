# Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com
# base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas
# daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana
# recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa (usando
# um array de contadores) que determine quantos vendedores receberam salários nos seguintes
# intervalos de valores:
# A. $200 - $299
# B. 300 - $399
# C. $400 - $499
# D. $500 - $599
# E. $600 - $699
# F. $700 - $799
# G. $800 - $899
# H. $900 - $999
# I. $1000 em diante
# Desafio: Crie uma fórmula para chegar na posição da lista a partir do salário, sem fazer
# vários ifs aninhados.
sal,contador = [], []
from random import randint
from typing import Counter
for b in range(100):
    sal.append(randint(200,1200))
for con in sal:
    calc = con // 100 - 2
    contador.append(calc)
    if calc > 8:
        contador.pop(sal.index(con))
        contador.append(8)
print(f'\nValores do contador: {contador}')
final = str(Counter(contador))
final = final.replace('Counter({', '')
final = final.replace('})', '')
print('\n> Legenda:\n- 0: $200 - $299\n- 1: $300 - $399\n- 2: $400 - $499\n- 3: $500 - $599\n- 4: $600 - $699\n- 5: $700 - $799\n- 6: $800 - $899\n- 7: $900 - $999\n- 8: $1000 > ')
print(f'\n>>> {final}')

