# A empresa Hipotheticus paga R$10,00 por hora normal trabalhada, e R$15,00 por
# hora extra. Faça um algoritmo para calcular e imprimir o salário bruto e o 
# salário líquido de um determinado funcionário. Considere que o salário líquido 
# é igual ao salário bruto descontando-se 10% de impostos.
salarioHora = 10
salarioExtra = 15

try:
    horasTrabalhadas = float(input('Insira a quantidade de horas trabalhadas no mês: '))
    while horasTrabalhadas > 730 or horasTrabalhadas < 0:
        print('Valor inválido.')
        horasTrabalhadas = float(input('Insira a quantidade de horas trabalhadas no mês: '))
except:
    exit(print('Error.'))
# 8 horas de trabalho por dia / 44 por semana / 220 por mês
if horasTrabalhadas > 220:
    horasExtra = horasTrabalhadas - 220
    salarioBruto = 220 * salarioHora
    salarioBruto = salarioBruto + (horasExtra*salarioExtra)
else:
    salarioBruto = horasTrabalhadas * salarioHora
    horasExtra = 'nenhuma'
imposto = 0.1 * salarioBruto
salarioLiquido = salarioBruto - imposto
print(f'\n> Considerando a jornada de trabalho de 220 h por mês...\n\n- Jornada de trabalho: {horasTrabalhadas} horas no mês.\n- Horas extra: {horasExtra}.\n- Salário bruto: R$ {salarioBruto}.\n- Salário líquido (10% imposto): R$ {salarioLiquido}.')