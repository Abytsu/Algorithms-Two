# Entrar com o dia e o mês de uma data e informar quantos dias se passaram desde o
# início do ano. Esqueça a questão dos anos bissextos e considere sempre que um mês
# possui 30 dias.
mes = 30
try:
    diaInput = (int(input('Informe o dia (máx 30): ')))
    mesInput = (int(input('Informe o mês: ')))
except:
    exit(print('Error.'))
while diaInput < 1 or diaInput > 30 or mesInput <1 or mesInput > 12:
    exit(print('Data inválida.'))
diasPassados = (mes*(mesInput-1)) + (diaInput-1)
print('{0} dias se passaram desde o início do ano.'.format(diasPassados))