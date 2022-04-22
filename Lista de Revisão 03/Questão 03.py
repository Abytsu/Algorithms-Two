# Escrever um algoritmo que gera e escreve os número impáres entre 100 e 200.
core,rep = 100,0
while core < 200:
    core += 1 
    if core%2 == 1:
        rep += 1 
        print('A {0}ª repetição ímpar é: {1} '.format(rep,core))