# Faça um programa que recebe três números do usuário, e identifica o maior através de uma função e o menor através de outra função.
x = float(input("Digite um número (1): "))
y = float(input("Digite um número (2): "))
z = float(input("Digite um número (3): "))
def maior(x,y,z):
    lista = [x,y,z]
    lista.sort(reverse=True)
    return lista[0]
def menor(x,y,z):
    listam = [x,y,z]
    listam.sort()
    return listam[0]
print(f'\n O maior valor é: {maior(x,y,z)}')
print(f' O menor valor é: {menor(x,y,z)}')