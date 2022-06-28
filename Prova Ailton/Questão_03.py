lista, cont, pares, quant_i = [],0,0,0
def esp():
    print('\n')
for x in range(6):
    lista.append(int(input(f'Digite o número da posição {x+1}: ')))
for par in lista:
    cont += 1
    if par % 2 == 0:
        print(f'\n> O número {par} é par. O qual está na posição {cont}')
        pares += par
    elif par % 2 == 1:
        print(f'\n> O número {par} é impar. O qual está na posição {cont}')
        quant_i += 1
esp()

print(f"> A soma dos números pares é: {pares}")
esp()
print(f"> A quantidade de números ímpares digitados é: {quant_i}")
esp()



