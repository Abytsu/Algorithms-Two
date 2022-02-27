# A fábrica de refrigerantes Meia-Cola vende seu produto em três formatos: lata de
# 350 ml, garrafa de 600 ml e garrafa de 2 litros. Se um comerciante compra uma
# determinada quantidade de cada formato, faça um algoritmo para calcular quantos
# litros de refrigerante ele comprou.
refri350, refri600, refri2L = 350, 600, 2000
try:
    qRefri350, qRefri600, qRefri2L = int(input('Informe a quantidade comprada de refrigerantes de 350 ml: ')), int(input('Informe a quantidade comprada de refrigerantes de 600 ml: ')), int(input('Informe a quantidade comprada de refrigerantes de 2 L: '))
    while qRefri350 <0 or qRefri600 <0 or qRefri2L <0:
        exit(print('Valor inválido.'))
except:
    exit(print('Error.'))
litrosTotal = (qRefri350 * refri350 + qRefri600 * refri600 + qRefri2L * refri2L)/1000
print(f'\n> A quantidade total de litros de refrigerante comprados é: {litrosTotal} L')