# Escrever um algoritmo que lê 5 valores para a, um de cada vez, e conta quantos destes valores
# são negativos, escrevendo essa informação.
negative = 0
for v in range(5):
    try:
        a = float(input('Digite um valor para a: '))
    except:
        exit(print('Error...'))
    if a < 0:
        negative += 1
if negative < 5 and negative != 0:
    print(f'\n> De todos os 5 valores inseridos, somente {negative} são negativos.')
elif negative == 0:
    print('\n> Nenhum valor é negativo.')
else:
    print('\n> Todos os valores são negativos.')
