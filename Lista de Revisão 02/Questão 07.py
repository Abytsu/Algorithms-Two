# Faça um Programa que leia três números e mostre-os em ordem decrescente
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
print('\n- Estes número em ordem decrescente ficam: {0}, {1} e {2}'.format(numlist[0], numlist[1], numlist[2]))