# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo
def error():
    exit(print('Error.'))
try: 
    num1 = float(input('Informe o número: '))
except:
    error()
if num1 > 0:
    sinal = 'positivo'
elif num1 <0:
    sinal = 'negativo'
else:
    sinal = 'neutro'
print('O número {0} é {1}.'.format(num1, sinal))