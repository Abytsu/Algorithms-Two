notas,soma_n = [],0
for alunos in range(15):
    notas.append(float(input(f'Insira a nota {alunos+1}: ')))
for soma in notas:
    soma_n += soma
media = soma_n / (alunos+1)
print(f"A média final é: {media}")