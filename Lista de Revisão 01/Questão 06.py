# Uma fábrica controla o tempo de trabalho sem acidente pela quantidade de dias.
# Faça um algoritmo para converter este tempo em anos, meses e dias. Assuma que
# cada mês possui sempre 30 dias.
mes = 30
ano = mes*12
try:
    diasSemAcidente = int(input('Quantos dias sem acidente na fábrica? '))
    if diasSemAcidente < 0:
        exit(print('Data inválida.'))
except:
    exit(print('Error.'))
if diasSemAcidente >= mes :
    mesSemAcidente = diasSemAcidente / mes
    mesS = mesSemAcidente
    if diasSemAcidente >= ano:
        anoSemAcidente = diasSemAcidente / ano
        anoS = anoSemAcidente
    else:
        anoS = 'nenhum'
else:
    anoS = 'nenhum'
    mesS = 'nenhum'
print('\n- {0} dias sem acidentes equivalem a:\n- {1} mes(es) sem acidente\n- {2} ano(s) sem acidente'.format(diasSemAcidente,mesS,anoS))

