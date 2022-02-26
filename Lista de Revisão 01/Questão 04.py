# O restaurante a quilo Bem-Bão cobra R$ 12,00 por cada quilo de refeição. Escreva um
# algoritmo que leia o peso do prato montado pelo ciente (em quilos) e imprima o valor
# a pagar. Assuma que a balança já desconte o peso do prato.
precoQuilo = 12.00
try:
    clientePrato = float(input('Quantos quilos o seu prato pesa? '))
    while clientePrato < 0:
        print('Valor inválido.\n')
        clientePrato = float(input('Quantos quilos o seu prato pesa? '))
except:
    exit(print('Error.'))
print(f'\n- O preço a pagar é de: R$ {(precoQuilo*clientePrato)}')
