# A lanchonete Gostosura vende apenas um tipo de sanduíchie, cujo recheio inclui
# duas fatias de queijo, uma fatia de presunto e uma rodela de hambúrguer. Sabendo
# que cada fatia de queijo ou presunto pesa 50 gramas, e que a rodela de hambúrguer
# pesa 100 gramas, faça um algoritmo em que o dono forneça a quantidade de
# sanduíches a fazer, e a máquina informe as quantidades (em quilos) de queijo, persunto
# e carne necessários para compra.
from itertools import count

fatiaQueijo, fatiaPresunto, rodelaHamburguer = 50 , 50, 100
sanduicheIngredientes = ('queijo', 'queijo', 'presunto', 'hamburguer')
try:
    quantSanduiche = int(input('Digite a quantidade de sanduíches à fazer: '))
    while quantSanduiche < 0:
        print('Valor inválido.')
        quantSanduiche = int(input('Digite a quantidade de sanduíches à fazer: '))
except:
    exit(print('Error.'))
sanduicheFazer = sanduicheIngredientes * quantSanduiche
quantQueijo, quantPresunto, quantHamburguer = sanduicheFazer.count('queijo'), sanduicheFazer.count('presunto'), sanduicheFazer.count('hamburguer')
queijoComprar, presuntoComprar, hamburguerComprar = quantQueijo * fatiaQueijo, quantPresunto * fatiaPresunto, quantHamburguer * rodelaHamburguer
print(f'\n> Para fazer {quantSanduiche} sanduíches, serão necessários:\n- {(queijoComprar/1000)} KG de queijo ({quantQueijo} fatias). \n- {(presuntoComprar/1000)} KG de presunto ({quantPresunto} fatias).\n- {(hamburguerComprar/1000)} KG de hambúrguer ({quantHamburguer} rodelas).')


