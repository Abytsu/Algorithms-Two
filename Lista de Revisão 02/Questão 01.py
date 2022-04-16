# Faça um Programa que peça dois números e imprima o maior deles.
def error():
    exit(print('Error.'))
try: 
    num1 = float(input('Insira o valor do primeiro número para comparação: '))
    num2 = float(input('Insira o valor do segundo número para comparação: '))
except:
    error()
if num1 > num2: 
    print(f'\nO número {num1} é maior que {num2}.')
elif num2 > num1:
    print(f'\nO número {num2} é maior que {num1}.')
else:
    print('Ambos os números têm o mesmo valor.')