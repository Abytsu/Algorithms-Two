# Faça um programa que leia duas listas e que gere uma terceira com os elementos das duas primeiras.
list1 = []
list2 = []
max = 0
while True:
  list1.append(input('|| Digite os elementos da lista 1: '))
  list2.append(input('|| Digite os elementos da lista 2: '))
  max += 1
  if list1[max-1] == '0' or list2[max-1] == '0':
    if list1[max-1] == '0':
        list1.pop(max-1)
    elif list2[max-1] == '0':
        list2.pop(max-1)
    break

list3 = list1+list2
print(f'|| A soma das lista é: {list3}')