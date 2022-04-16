# Faça um Programa que leia três números e mostre o maior e o menor deles
def error():
    exit(print('Error.'))
try: 
    num1 = float(input('> Insira o valor do primeiro número: '))
    num2 = float(input('> Insira o valor do segundo número: '))
    num3 = float(input('> Insira o valor do terceiro número: '))
except:
    error()
numlist = [float(num1), float(num2), float(num3)]
numlist.sort(reverse=True)
print(f'O maior valor inserido é \033[32m{numlist[0]}\033[m, enquanto o menor valor é \033[31m{numlist[2]}\033[m')
if num1 == num2 and num2 == num3:
    print('Os valores são iguais.')