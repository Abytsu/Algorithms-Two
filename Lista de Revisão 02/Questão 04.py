# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.
def error():
    exit(print('Error.'))
try: 
    nota1 = float(input('> Insira o valor da primeira nota parcial: '))
    nota2 = float(input('> Insira o valor da segunda nota parcial: '))
except:
    error()
media_aluno = ((nota1+nota2)/2)
if media_aluno >= 7:
    aprovacao_estado = '\033[32mAprovado\033[m'
    if media_aluno >= 10:
        aprovacao_estado = '\033[34mAprovado com Distinção\033[m'
elif media_aluno < 7:
    aprovacao_estado = '\033[31mReprovado\033[m'
else:
    aprovacao_estado = 'Não foi possível calcular'
if media_aluno > 10:
    media_aluno = 10
elif media_aluno <0:
    media_aluno = 0
print(f'\n O aluno com as seguintes notas:\n- Nota 1: {nota1}\n- Nota 2: {nota2}\n- Com média: {media_aluno}.\n > Se encontra no estado: {aprovacao_estado}')
