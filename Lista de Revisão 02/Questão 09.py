# Faça um Programa que peça um número inteiro e determine se ele é par ou ímpar. Dica:
# utilize o operador módulo (resto da divisão)
def error():
    exit(print('Error: valor inválido ou o número não é \033[4;31mINTEIRO\033[m.'))
try: 
    num = int(input('Insira o valor de um número INTEIRO para classificá-lo como par ou ímpar: '))
except:
    error()
parImpar = num%2
if parImpar == 0:
    numEst = 'par'
elif parImpar == 1:
    numEst = 'ímpar'
else:
    numEst = 'error'
print('\n> O número {0} é {1}.'.format(num, numEst))