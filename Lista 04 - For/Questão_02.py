# Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões
# o programa deve perguntar ao aluno qa resposta de cada questão e ao final comparar
# com o gabarito da prova e assim calcular o total de acertos e a nota (atribui
# um ponto por respota certa. Após cada aluno utilizar o sistema ser feita uma
# pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido
# informar:
# a. Maior e Menor Acerto;
# b. Total de Alunos que utilizaram o sistema;
# c. A média das Notas da turma.
tomada, utilizacao, pontoTotal, ponto, pontoMax, pontoMin, sessaoMax, sessaoMin, totalMin, totalMax, max, min = 0,0,0,0,0,0,0,0,0,0,0,0
while tomada != 1:
    for v in range(1):
        ponto = 0
        print('\nBem-vindo(a) ao sistema de notas! Comecando a prova...\n> OBS: digite no terminal somente as letras das alternativas, não a questão completa.')
        try:
            q1=str(input('\n\n# Questão 01 (Michel Concursos - 2022)\n- A palavra reservada, utilizada no Python, que permite a repetição de forma ilimitada é:\na) For.\nb) While.\nc) Range.\nd) If.\n\n> Sua resposta: '))
            q2=str(input('\n\n# Questão 02 (FCM - 2022)\n- A respeito dos componentes de um computador, é correto afirmar que o termo "Core i7 da Intel" refere-se a um tipo de\na) SSD.\nb) disco rígido.\nc) processador.\nd) memória RAM.\n\n> Sua resposta: '))
            q3=str(input('\n\n# Questão 03 (Michel Concursos - 2012\n> if preco < 40:\n>\tprint("ótimo preço para comprar o produto")\n- O bloco de código acima expressa:\na) se o preço for menor que 40, o usuário é sugerido a comprar. \nb) se o preço for igual a 40, o usuário é sugerido a não comprar. \nc) se o preço for maior que 40, o usuário deve comprar. \nd) se o preço for menor que 40, o usuário deve vender o produto.\n\n> Sua resposta: '))
            q4=str(input('\n\n# Questão 04 (Michel Concursos - 2010)\n- Qual a funcionalidade da palavra reservada "for" na linguagem Python?\na) Atribuir um valor fixo a uma variável. \nb) Apagar o comando anterior.\nc) Repetir um bloco de código de forma limitada.\nd) Repetir um bloco de código de forma ilimitada.\n\n> Sua resposta: '))
            q5=str(input('\n\n# Questão 05 (Michel Concursos - 2022)\n- A operação "40%2"...\na) Divide 40 por 2. \nb) Calcula o resto de 40 por 2.\nc) Calcula a porcentagem de 40.\nd) Multiplica e depois divide 40 por 2.\n\n> Sua resposta: '))
            q6=str(input('\n\n# Questão 06 (Instituto UniFil - 2021)\n- Assinale a alternativa que não define uma das características de Software Livre.\na) Possui código aberto.\nb) Concede liberdade ao usuário para executar, acessar e modificar seu código.\nc) Permite redistribuir cópias com ou sem modificações do seu código.\nd) Considerado Software Proprietário.\n\n> Sua resposta: '))
            q7=str(input('\n\n# Questão 07 (Michel Concursos - 2018)\n- Qual das alternativas apresenta um software proprietário?\na) GIMP. \nb) LibreOffice.\nc) Photoshop.\nd) VLC.\n\n> Sua resposta: '))
            q8=str(input('\n\n# Questão 08 (Michel Concursos - 2010)\n- O que acontece se você apertar as teclas Alt + F4 no Windows enquanto estiver usando um programa?\na) O programa irá fechar. \nb) O programa irá minimizar.\nc) O programa irá para a memória RAM.\nd) Não acontecerá nada.\n\n> Sua resposta: '))
            q9=str(input('\n\n# Questão 09 (TCE/SP: FCC - 2021)\n- O armazenamento de informações em computadores é feito pela utilização de dispositivos chamados de memória, que as mantêm de forma volátil ou permanente. Entre esses dispositivos, está a memória RAM ou memória\na) magnética. \nb) secundária.\nc) cache.\nd) principal.\n\n> Sua resposta: '))
            q10=str(input('\n\n# Questão 10 ( Michel Concursos - 1845)\n- Assinale a alternativa que NÃO indique um exemplo de uma memória não volátil.\na) Memória RAM.\nb) ROM ou Memória de Somente Leitura\nc) Hard Disk ou Disco Rígido.\nd) SSD ou Solid State Drive.\n\n> Sua resposta: '))
        except:
            q1, q2, q3, q4, q5, q6, q7, q8, q9, q10 = 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 
            print('Comando inserido não foi reconhecido pelo sistema. A prova foi anulada e sua nota será zero!')
    utilizacao += 1
    try:
        if q1[0].lower() == 'b':
            ponto += 1
        if q2[0].lower() == 'c':
            ponto += 1
        if q3[0].lower() == 'a':
            ponto += 1
        if q4[0].lower() == 'c':
            ponto += 1
        if q5[0].lower() == 'b':
            ponto += 1
        if q6[0].lower() == 'd':
            ponto += 1
        if q7[0].lower() == 'c':
            ponto += 1
        if q8[0].lower() == 'a':
            ponto += 1
        if q9[0].lower() == 'd':
            ponto += 1
        if q10[0].lower() == 'a':
            ponto += 1
    except:
        ponto = 0
        print('\n>>> Ocorreu um erro no cálculo da sua nota. A nota atribuída será zero! Tente novamente.')
    print(f'\n> O total de pontos que voce conseguiu foi: {ponto} pontos (prova vale 10 pontos)\n> O sistema está sendo usado pela {utilizacao}ª vez.\n')
    pontoTotal += ponto
    pontoMaximo = pontoMax
    pontoMinimo = pontoMin
    if utilizacao == 1:
        pontoMaximo, pontoMinimo, pontoMax, pontoMin, totalMax, totalMin = ponto, ponto, ponto, ponto, ponto, ponto
        sessaoMax, sessaoMin, max, min = utilizacao, utilizacao, utilizacao, utilizacao
    if ponto > pontoMaximo:
        pontoMax = ponto
        sessaoMax = utilizacao
        totalMax += pontoMax
        max += 1
    elif ponto < pontoMinimo:
        pontoMin = ponto
        sessaoMin = utilizacao
        totalMin += pontoMin
        min += 1
    else:
        pontoMin, pontoMax = pontoMin, pontoMaximo
    try:
        decisao = str(input('Deseja terminar o programa? S/N\n> '))
        decisaoSN = decisao[0].upper()
    except:
        print('Comando não reconhecido. O programa continuará normalmente.')
        decisaoSN = 'x'
    if decisaoSN == 'S':
        tomada = 1
    if tomada == 1:
        menor = pontoMin
        maior = pontoMax
        media = pontoTotal / utilizacao
        mediaMaior = pontoMax / max
        mediaMenor = pontoMin / min
print('\n\n{:-^90}'.format(' Sistema Finalizado '))
print('\n{:#^75}'.format(' Resumo sobre a utilização do programa '))
print(f'\n> O sistema foi utilizado {utilizacao} vezes.\n> O total de pontos de todas as provas foi de {pontoTotal} pontos.\n\n> A maior nota foi {maior} na {sessaoMax}ª sessão do programa.\n> A menor nota foi {menor} na {sessaoMin}ª sessão do programa.\n\n> A média total das provas é: {media}\n> A média das maiores notas é: {mediaMaior}\n> A média das menores notas é: {mediaMenor}\n\n---> Obrigado por utilizar!')
# gabarito 
# 1 - b
# 2 - c
# 3 - a
# 4 - c
# 5 - b
# 6 - d
# 7 - c
# 8 - a
# 9 - d
# 10 - a