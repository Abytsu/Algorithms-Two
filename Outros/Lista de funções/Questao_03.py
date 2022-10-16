# Crie uma função que recebe um inteiro positivo e teste para saber se ele é primo ou não. Faça um script que 
# recebe um inteiro n e mostra todos os primos de 1 até n.
def primor(x):
    for v in range(2, x):
        if x % v == 0:
            return print('Não é primo')
    else:
        print('é primo')
x = int(input('Digite: '))
primor(x)