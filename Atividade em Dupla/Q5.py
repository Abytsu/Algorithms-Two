# Escreva uma função que receba uma string e uma lista. A função deve comparar a string
# passada com os elementos da lista, também passada como parâmetro. 
# Retorne verdadeiro se a string for encontrada dentro da lista, e falso, caso contráro.
listaTeste = ['Marcelo', 25, 'Café', 'Queijo', 12]
def comparer(string,lista):
    print(f'{string} na lista é:')
    for checksum in lista:
        if string in lista:
            return print('Verdadeiro\n')
        elif string not in lista:
            return print('Falso\n')
comparer('Queijo', listaTeste)
comparer('Café', listaTeste)
comparer('Presunto', listaTeste)
comparer(12, listaTeste)