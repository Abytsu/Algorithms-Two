# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e
# os números.
vetor = []
soma, mult, multer = 0,1,0
for c in range(5):
    vetor.append(int(input(f'Insira o valor {c+1} da lista: ')))
for s in range(len(vetor)):
    soma += vetor[s]
for m in range(len(vetor)):
    mult = mult * vetor[m]
print(f'\n- A soma dos números inseridos é: {soma}')
print(f'\n- A múltiplicação dos números inseridos é: {mult}')
print(f'\n- Os números inseridos são:')
for n in vetor:
    print(f'> {n}')