# Faça um programa que leia números reais maiores que zero, Quando for entrado o número zero,
# o programa deverá apresentar quantos números foram entrados e a média destes.
core,times,total = 0,0,0
while core != 1:
    userInput = float(input('Digite qualquer número real não negativo, digite 0 para sair: '))
    while userInput < 0:
        print(f'O número {userInput} é negativo.')
        userInput = float(input('Digite qualquer número real maior que zero: '))
    if userInput == 0:
        core = 1
    else:
        total = userInput + total
        times += 1 
        med = total/times
print('\nForam reconhecidas {0} entradas de números que atendem os requisitos.\n> A média destes é: {1}'.format(times,med))


