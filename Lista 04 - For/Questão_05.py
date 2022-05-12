# Faça um algoritmo que leia as três notas de 50 alunos de uma turma, para cada aluno, calcule a média
# ponderada, como segue: MP = (n1*2 + n2*4 + n3*3)/10
aluno = 1
for v in range(50):
    n1 = float(input(f'Digite a nota 1 do aluno {aluno}: '))
    n2 = float(input(f'Digite a nota 2 do aluno {aluno}: '))
    n3 = float(input(f'Digite a nota 3 do aluno {aluno}: '))
    mp = (n1*2 + n2*4 + n3*3)/9
    print(f'A média ponderada das notas do aluno {aluno}, é: {mp}')
    aluno += 1