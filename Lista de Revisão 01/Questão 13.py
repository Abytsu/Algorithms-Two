# Uma confecção produz X blusas de lã e para isto gasta uma certa quantidade de
# novelos. Faça um algoritmo para calcular quantos novelos de lá ela gasta por blusa.
try:
    blusas = int(input('Quantas blusas foram produzidas? '))
    novelos = float(input('Quantos novelos foram utilizados? '))
    while blusas < 0 or novelos < 0:
        print('Valor inválido.')
        blusas = int(input('Quantas blusas foram produzidas? '))
        novelos = float(input('Quantos novelos foram utilizados? '))
except:
    exit(print('Error.'))
novelosPorBlusa = novelos / blusas
print(f'\n> Para cada blusa, é necessário {novelosPorBlusa} novelos.')
