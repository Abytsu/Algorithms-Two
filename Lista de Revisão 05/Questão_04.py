# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As
# perguntas são:
# A."Telefonou para a vítima?"
# B."Esteve no local do crime?"
# C."Mora perto da vítima?"
# D."Devia para a vítima?"
# E."Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a
# pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4
# como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
qst,ans,pts = ["Telefonou para a vítima? ", "Esteve no local do crime? ", "Mora perto da vítima? ", "Devia para a vítima? ", "Já trabalhou com a vítima? "],[],0
for q in range(len(qst)):
    print('\n> responda com S ou N:')
    ans.append(str(input(qst[q])))
    ver = (ans[q].lower())[0]
    if ver == 's':
        pts += 1
if pts == 2:
    print('\n> Você é suspeito(a)!')
elif pts > 2 and pts < 5:
    print('\n >Você é cúmplice!')
elif pts >= 5:
    print('\n> Você é o(a) assasino(a)!')
else:
    print('\n> Você é inocente!')