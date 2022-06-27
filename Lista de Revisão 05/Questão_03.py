# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em
# uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima
# da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro,
# . . . ).
temp_anos = []
total_temp = 0
from random import randint
for a in range(1,13):
    temp_anos.append(float(input(f'Temperatura do mês {a}? ')))
    total_temp = temp_anos[a-1] + total_temp
media_temp = total_temp/a
for teste in range(len(temp_anos)):
    if temp_anos[teste] > media_temp:
        indexo = teste + 1
        if indexo == 1:
            mes = 'Janeiro'
        if indexo == 2:
            mes = 'Fevereiro'
        if indexo == 3:
            mes = 'Março'
        if indexo == 4:
            mes = 'Abril'
        if indexo == 5:
            mes = 'Maio'
        if indexo == 6:
            mes = 'Junho'
        if indexo == 7:
            mes = 'Julho'
        if indexo == 8:
            mes = 'Agosto'
        if indexo == 9:
            mes = 'Setembro'
        if indexo == 10:
            mes = 'Outubro'
        if indexo == 11:
            mes = 'Novembro'
        if indexo == 12:
            mes = 'Dezembro'
        print(f'\n> A temperatura {temp_anos[teste]}° está acima da média e ocorreu no mês de {mes}')
print(f'\n\t> Média de temperatura anual:{media_temp}°')

