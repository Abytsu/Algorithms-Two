# Faça um programa que pergunte o preço de três produtos e informe qual produto você
# deve comprar, sabendo que a decisão é sempre pelo mais barato.
def error():
    exit(print('Error.'))
try: 
    prod1 = float(input('> Insira o valor do primeiro produto: '))
    while prod1 < 0:
        print('O produto não pode possuir valor negativo, tente novamente.\n')
        prod1 = float(input('> Insira o valor do primeiro produto: '))
    prod2 = float(input('> Insira o valor do segundo produto: '))
    while prod2 < 0:
        print('O produto não pode possuir valor negativo, tente novamente.\n')
        prod2 = float(input('> Insira o valor do segundo produto: '))
    prod3 = float(input('> Insira o valor do terceiro produto: '))
    while prod3 < 0:
        print('O produto não pode possuir valor negativo, tente novamente.\n')
        prod3 = float(input('> Insira o valor do terceiro produto: '))
except:
    error()
prodList = [prod1, prod2, prod3]
prodList.sort()
if prod1 == prod2 and prod2 == prod3:
    prod = 'todos têm o mesmo valor'
elif prod1 == prodList[0]:
    prod = 'primeiro'
elif prod2 == prodList[0]:
    prod = 'segundo'
elif prod3 == prodList[0]:
    prod = 'terceiro'
else:
    prod = 'algo deu errado'
print('\n- Você deve comprar o \033[1;33m{0}\033[m produto, pois é o mais barato. Seu valor é: \033[1;32mR$ {1}\033[m.'.format(prod, prodList[0]))