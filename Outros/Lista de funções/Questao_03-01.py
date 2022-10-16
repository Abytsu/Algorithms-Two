# Crie uma função que recebe um inteiro positivo e teste para saber se ele é primo ou não. Faça um script que 
# recebe um inteiro n e mostra todos os primos de 1 até n.
def primor(x):
    for v in range(2, x):
        if v == 2:
            print(2)    
        if v == 3:
            print(3)
        if v == 5:
            print(5)
        if v == 7:
            print(7)
        if v % 2 > 0 and v % 3 > 0 and v % 5 > 0 and v % 7:
            print(v)
x = int(input('Digite: '))
primor(x)