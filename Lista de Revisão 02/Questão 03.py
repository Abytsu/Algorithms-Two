# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido
letra = str(input('Informe qual o seu sexo (M ou F): '))
sexo=letra[0].upper()
if sexo == 'F':
    sexo = 'feminino.'
elif sexo == 'M':
    sexo = 'masculino.'
else:
    sexo = 'sexo inválido.'
print('O sexo informado foi: {0}'.format(sexo))