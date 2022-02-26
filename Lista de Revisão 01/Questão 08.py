# Calcue a área de uma pizza que possui um raio R (pi=3.14)
try:
    pizzaRaio = float(input('Informe o raio da Pizza: '))
    while pizzaRaio <0:
        print('Valor inválido.')
        pizzaRaio = float(input('Informe o raio da Pizza: '))
except:
    exit(print('Error.'))
pizzaArea = 3.14*(pizzaRaio**2)
print(f'\n- A área desta pizza é de: {pizzaArea} cm²')