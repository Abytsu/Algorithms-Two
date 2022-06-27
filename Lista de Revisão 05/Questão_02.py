# Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos
# alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.
import random
qnt_aluno = 30
idade,altura = [], []
soma_altura = 0
aluno_pequeno = 0
for i in range(qnt_aluno):
    idade.append(random.randint(4,18))
for a in range(qnt_aluno):
    altura.append(random.uniform(1,2))
for m in altura:
    soma_altura += m 
media_h = soma_altura /30
media_hs = str(media_h)
for t in range(len(idade)):
    if idade[t] > 13:
        if altura[t] < media_h:
            aluno_pequeno += 1
            print(f'> O aluno na posição {t+1} possui a altura menor do que a média')
            haltura = str(altura[t])
            print(f'--> Altura: {haltura[0:4]}\n')
print(f'> Total de alunos de 13 anos com a altura menor que a média: {aluno_pequeno} alunos')
print(f'> Média de altura: {media_hs[0:4]}')
