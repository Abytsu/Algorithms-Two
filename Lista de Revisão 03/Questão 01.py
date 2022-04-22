# Desenvolver um algoritmo que leia a altura de 15 pessoas. Este programa deverá calcular e
# mostrar:
# a. A menor altura do grupo;
# b. A maior altura do grupo
rep, altura, alturaA, alturaB = 0,0,0,0
while rep < 15:
    alturaAlto = alturaA
    alturaBaixo = alturaB
    altura = float(input('Qual a altura da pessoa {0}? '.format(rep+1)))
    while altura < 0:
        print('Não existe altura negativa.')
        altura = float(input('Qual a altura da pessoa {0}? '.format(rep+1)))
    if rep == 0:
        alturaBaixo, alturaAlto = altura, altura
    if altura < alturaBaixo:
        alturaB = altura
    elif altura > alturaAlto:
        alturaA = altura
    else:
        alturaB, alturaA = alturaBaixo, alturaAlto
    if rep == 14:
        menor = alturaB
        maior = alturaA
    rep = rep + 1
print('A maior pessoa do grupo mede: {0} m\nEnquanto a menor pessoa mede: {1} m'.format(maior, menor))