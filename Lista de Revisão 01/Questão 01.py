# A imobiliária Imóbilis vende apenas terrenos retangulares. Faça um algoritmo para ler as dimensões de um terreno e depois exibir a área do terreno.
try:
    lado1 = float(input('Digite a largura do terreno em metros: '))
    lado2 = float(input('Digite a profundidade do terreno em metros: '))
except:
    exit(print('Error'))
if lado1 < 0 or lado2 < 0:
    exit(print('Não existe medida negativa.'))
area = lado1 * lado2 
print(f'A área do seu terreno é de: {area} m²')