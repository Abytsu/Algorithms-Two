temp_ano,temp_t,c,mes = [],0,0,0
for ano in range(12):
    temp_ano.append(int(input(f'> Insira a temperatura média do mês {ano+1}: ')))
    temp_t += temp_ano[ano]
media_a = temp_t / (ano+1)

for m in temp_ano:
    c += 1
    if m > media_a:
        if c == 1:
            mes = 'Janeiro'
        if c == 2:
            mes = 'Fevereiro'
        if c == 3:
            mes = 'Março'
        if c == 4:
            mes = 'Abril'
        if c == 5:
            mes = 'Maio'
        if c == 6:
            mes = 'Junho'
        if c == 7: 
            mes = 'Julho'
        if c == 8:
            mes = 'Agosto'
        if c == 9:
            mes = 'Setembro'
        if c == 10:
            mes = 'Outubro'
        if c == 11:
            mes = 'Novembro'
        if c == 12:
            mes = 'Dezembro'
        print(f'\nA temperatura de {m}° C está acima da média e se encontra no mês de {mes}')
media_bonita = (((media_a * 100) // 1) / 100)
print(f'\n> A média da temperatura é: {media_bonita}° C')
