# A probabilidade de dar um valor em um dado é 1/6 (uma em 6). Faça um script com função em Python que 
# simule n vezes de lançamentos de dados e mostre a frequência que deu para cada número
import random
dice = []
def dado(vezes):
    counter = 1
    for v in range(vezes):
        dice.append(random.randint(1,6))
    for v in range(6):
        print(f'- A face {counter} caiu {dice.count(counter)} vezes')
        counter += 1
dado(659)