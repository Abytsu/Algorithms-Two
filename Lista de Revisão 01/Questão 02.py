# Faça um algoritmo para calcular quantas ferraduras são necessárias para equipar todos os vacalos comprados para um haras
patas_cavalo = 4
try:
    cavalos = int(input('Quantos cavalos compõem o haras?\n> '))
except:
    exit(print('Error'))
ferraduras = cavalos * patas_cavalo
if cavalos > 1:
    c = 's.'
elif cavalos == 1:
    c = '.'
else:
    c= '?'
print('Serão necessárias', ferraduras,'ferraduras para', cavalos,'cavalo'+c)