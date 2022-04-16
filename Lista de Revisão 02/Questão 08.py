# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M -matutino
# ou V -Vespertino ou N - Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa
# Noite!" ou "Valor Inválido!", conforme o caso.
turno = str(input('Olá! Qual turno você estuda?\n- M: Matutino;\n- V: Vespertino;\n- N: Noturno.\n> '))
turnoC=turno[0].upper()
if turnoC[0] == 'M':
    print('\nBom Dia!')
elif turnoC[0] == 'V':
    print('\nBoa Tarde!')
elif turnoC[0] == 'N':
    print('\nBoa noite!')
else:
    print('\nValor Inválido!')
