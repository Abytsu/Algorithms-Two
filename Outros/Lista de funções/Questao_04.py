# Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais:
# taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do impsoto.
# A função "altera" o valor de custo para incluir imposto sobre vendas.
def somaImposto(taxaImposto, custo):
    return custo + ((taxaImposto/100)*custo)
x = float(input('Digite a taxa do imposto (em porcentagem): '))
y = float(input('Digite o custo do produto: '))
print(f'O produto com a taxa de imposto somada é: {somaImposto(x,y)} R$')