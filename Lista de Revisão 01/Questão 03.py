# A padaria Hotpão vende uma certa quantidade de pães franceses e uma quantidade de broas a cada dia. Cada pãozinho custa R$ 0,12 e 
# a broa custa R$ 1,50. Ao final do dia, o dono quer saber quanto arrecadou com a venda dos pães e broas (juntos), e quanto deve
# guardar numa conta de poupança (10% do total arrecadado). Você foi contratado para fazer os cálculos para o dono. Com base nestes
# fatos, faça um algoritmo para ler as quantidades de pães e de broas, e depois calcular os dados solicitados.
pao, broa = 0.12, 1.50
try: 
    quantPao = int(input('Quantos pães franceses foram vendidos hoje? '))
    quantBroa = int(input('Quantas broas foram vendidas hoje? '))
except:
    exit(print('Error.'))
if quantBroa < 0 or quantPao < 0:
    exit(print('Não é possível vender uma quantidade negativa.'))
print(f'\n\t\t - Lucros do dia -\n\n- Pães vendidos: {quantPao}\n- Valor arrecadado: R$ {(pao*quantPao)}\n\n- Broas vendidas: {quantBroa}\n- Valor arrecadado: R$ {(broa*quantBroa)}\n\n- Valor total:R$ {((broa*quantBroa)+(pao*quantPao))}\n- Poupança (10%): R$ {(((broa*quantBroa)+(pao*quantPao))*0.1)}')