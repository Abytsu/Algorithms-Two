# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
# Ex.: 5!=5.4.3.2.1 = 120
fatorial = 1
try:
    num = int(input('Digite um número inteiro para calcular o seu fatorial: '))
except:
    exit(print('Valor inválido, tente novamente.'))
for v in range(num):
    fatorial = fatorial * (v+1)
print(f'> Fatorial de {num} é: {fatorial}')