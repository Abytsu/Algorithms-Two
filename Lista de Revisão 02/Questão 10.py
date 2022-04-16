# Uma empresa resolver dar um aumento de salário aos seus colaboradores e lhe
# contrataram para desenvolver o programa que calculará os reajustes.
# > Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte
#   critério, baseado no salário atual:
# - salários até R$ 280,00 (incluindo): aumento de 20%
# - salários entre R$ 280.00 e R$ 700,00: aumento de 15%
# - salários entre R$ 700,00 e R$ 1500,00: aumento de 10%
# - salários de R$ 1500,00 em diante: aumento de 5%
# Após o aumento ser realizado, informe na tela:
# - o salário antes do reajuste;
# - o percentual do aumento aplicado;
# - o valor do aumento;
# - o novo salário, após o aumento.
def error():
    exit(print('\033[1;31mERROR!\033[m'))
try: 
    salario = float(input('> Insira o valor do salário do funcionário (em R$): '))
except:
    error()
if salario <= 280:
    grauReajuste = 1
elif salario > 280 and salario < 700:
    grauReajuste = 2
elif salario >= 700 and salario < 1500:
    grauReajuste = 3
elif salario >= 1500:
    grauReajuste = 4
def reajuste(grauReajuste):
    if grauReajuste == 1:
        porcentagem = 0.20
    elif grauReajuste == 2:
        porcentagem = 0.15
    elif grauReajuste == 3:
        porcentagem = 0.10
    elif grauReajuste == 4:
        porcentagem = 0.05   
    percentualAumento = porcentagem
    valorAumento = salario * percentualAumento
    salarioFinal = salario + valorAumento
    return salario, percentualAumento, valorAumento, salarioFinal
class cores:
    dinheiro = "\033[1;92m"
    porcent = "\033[1;94m"
    fim = "\033[m"
dadosFinais = reajuste(grauReajuste)
print(f'\n > Resumo do Reajuste de Salário\n\n- Salário antes do reajuste: {cores.dinheiro}R$ {dadosFinais[0]}{cores.fim}\n- Percentual do aumento: {cores.porcent}{int(dadosFinais[1]*100)} %{cores.fim}\n- Valor do aumento: R$ {cores.dinheiro}{dadosFinais[2]}{cores.fim}\n- Salário após o aumento: {cores.dinheiro}R$ {dadosFinais[3]}{cores.fim}.')


