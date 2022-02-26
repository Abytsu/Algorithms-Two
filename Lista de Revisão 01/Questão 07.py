# Faça um algoritmo para ler o salário de um funcionário e aumentá-lo em 15%. Após
# o aumento, desconte 8% de impostos. Imprima o salário inicial, o salário com o
# aumento e o salário final.
try:
    salarioInicial = float(input('Digite o salário do funcionário (R$): '))
    while salarioInicial < 0:
        print('Valor inválido.')
        salarioInicial = float(input('Digite o salário do funcionário (R$): '))
except:
    exit(print('Error.'))
aumentoSalario = salarioInicial * 0.15
impostoSalario = salarioInicial * 0.08
print(f'\n- O salário do funcionário era de: R$ {salarioInicial}.\n- Com um aumento de 15%, ficou: R$ {(salarioInicial+aumentoSalario)}.\n- Com impostos de 8%, o salário final fica: R$ {((salarioInicial+aumentoSalario)-impostoSalario)}')
