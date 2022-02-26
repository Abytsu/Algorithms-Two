# Três amigos, Carlos, André e Felipe. Decidiram rachar igualmente a conta de um bar.
# Faça um algoritmo para ler o valor total da conta e imprimir quanto cada um deve
# pagar, mas faça com que Carlos e André não paguem centavos. Ex: uma conta de 
# R$101,53 resulta em R$33,00 para Carlos, R$33,00 para André e R$35,53 para Felipe.
try:
    contaTotal = float(input('Digite o valor da conta do bar (R$): '))
    while contaTotal < 0:
        print('Valor inválido.')
        contaTotal = float(input('Digite o valor da conta do bar (R$): '))
except:
    exit(print('Error.'))
contaDividida = contaTotal//3
valorAndre = contaDividida
valorFelipe = contaDividida + (contaTotal%3)
diferencaValor = valorFelipe - contaDividida
if diferencaValor >= 2:
    valorFelipe -= 1
    valorAndre += 1

print(f'\n- O valor que Carlos pagará é de: R$ {contaDividida}.\n- O valor que André pagará é de: R$ {valorAndre}\n- O valor que Felipe pagará é de: R$ {valorFelipe}')
