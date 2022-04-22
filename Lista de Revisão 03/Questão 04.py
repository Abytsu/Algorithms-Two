# Escrever um algoritmo que leia uma quantidade desconhecida de números e conte quantos deles
# estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deve
# terminar quando for lido um número negativo.
core,intr1,intr2,intr3,intr4,intr5 = 0,0,0,0,0,0
while core != 1:
    num = float(input('Digite um número qualquer de 0 a 100. Caso deseje sair, digite um número negativo.\n> '))
    if num < 0:
        core = 1
    elif num > 0:
        if num >= 0 and num <= 25:
            intr1 += 1
        elif num >= 26 and num <= 50:
            intr2 += 1
        elif num >= 51 and num <= 75:
            intr3 += 1
        elif num >= 76 and num <= 100:
            intr4 += 1
        else:
            intr5 += 1
print('O número de vezes que os seguintes intervalos foram reconhecidos:\n> Entre 0-25: {0}\n> Entre 26-50: {1}\n> Entre 51-75: {2}\n> Entre 76-100: {3}\n> Mais que 100: {4}'.format(intr1,intr2,intr3,intr4,intr5))