# A granja Frangotech possui um controle automatizado de cada frango da sua
# produção. No pé direito do frango há um anel com um chip de identificação; no pé
# esquerdo são dois anéis para indicar o tipo de alimento que ele deve consumir.
# Sabendo que o anel com chip custa R$4,00 e o anel de alimento custa R$3,50, faça um
# algoritmo para calcular o gasto total da granja para marcar todos os seus frangos.
anelChip, anelComida = 4.00, 3.50
frango = (anelChip, anelComida, anelComida)
try:
    frangoQuant = int(input('Insira a quantidade de galinhas na granja: '))
    while frangoQuant < 0:
        print('Valor inválido.')
        frangoQuant = int(input('Insira a quantidade de galinhas na granja: '))
except:
    exit(print('Error.'))
granja = frango * frangoQuant
granjaChip, granjaComida = granja.count(anelChip), granja.count(anelComida)
valorChip, valorComida = granjaChip*anelChip, granjaComida*anelComida
print(f'\n> Gastos da empresa Frangotech:\n\n- Quantidade de frangos: {frangoQuant}.\n- Gastos com anel de chip: R$ {valorChip}.\n- Quantidade de anéis: {granjaChip}.\n- Gastos com anel de comida: R$ {valorComida}.\n- Quantidade de anéis: {granjaComida}.\n- Gasto total: R$ {valorChip+valorComida}')