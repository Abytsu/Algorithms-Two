# Faça um programa que percorra duas listas e gere uma terceira sem elementos repetidos.
list1 = []
list2 = []
listaCorretora = []
max = 0
while True:
  list1.append(input('|| Digite os elementos da lista 1: '))
  list2.append(input('|| Digite os elementos da lista 2 (0 para sair): '))
  max += 1
  if list2[max-1] == '0':
    list1.pop(max-1)
    break
list3 = list1 + list2
for check in list3:
    if check not in listaCorretora:
        listaCorretora.append(check)
print(f'Lista 1 e Lista 2 sem elementos repetidos: {listaCorretora}')