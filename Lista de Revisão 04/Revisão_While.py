# A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o salário e número de filhos. A prefeitura deseja saber:
# a) média do salário da população;
# b) média do número de filhos;
# c) maior salário;
# d) percentual de pessoas com salário até R$100,00.

trigger, repetition, highSalario, highFamily, filhosQnt, pessoas100, salarioTotal, filhosTotal = 0,0,0,0,0,0,0,0
while trigger == 0:
    try:
        repetition += 1
        salario = float(input(f'> Informe o salário da família {repetition} (digite um valor negativo para finalizar o programa). '))
        if salario > 0 and salario < 100:
            pessoas100 += 1
        if salario < 0:
            salario, filhos == -255, -255
            trigger = 1
            repetition -= 1 
        else:
            salarioTotal += salario
            filhos = int(input(f'> Informe a quantidade de filhos da família {repetition}. '))  
            while filhos < 0:
                filhos = int(input(f'\n---> Não pode ser negativo.\n> Informe a quantidade de filhos da família {repetition}. '))
            if filhos > 0:
                filhosQnt += 1
                filhosTotal += filhos
    except:
        print('\n---> Entrada não validada, ocorreu um erro no programa. O sistema não armazenou os dados anteriores, tente novamente.\n')
        repetition -= 1
        salarioTotal -= salario
        filhosTotal -= filhos
        salario, filhos = -255, -255
    salarioArmaz = highSalario
    if repetition == 1:
        salarioArmaz, highSalario, highFamily == salario, salario, repetition
    if salario == -255 or filhos == -255:
        print
    elif salarioArmaz < salario:
        highSalario = salario
        highFamily = repetition
mediaSalario = salarioTotal / repetition
mediaFilhos = filhosTotal / filhosQnt
mediaPessoas100 = (pessoas100/repetition)*100
if mediaFilhos / int(mediaFilhos) >= 0.5:
    mediaFilhos = mediaFilhos + mediaFilhos/int(mediaFilhos)
print('\n\n{:#^90}'.format(' Informação sobre a população '))
print(f'\n> O número total de salário de todas as {repetition} famílias é de: R$ {salarioTotal}\n> Junto de: {filhosTotal} filhos.\n\n> O maior salário informado foi o de R$ {highSalario} na {highFamily}ª família.\n\n> Média dos salários: R$ {mediaSalario}\n> Média de filhos: {int(mediaFilhos)}\n> Porcentagem de pessoas com salário até R$ 100: {mediaPessoas100}%')