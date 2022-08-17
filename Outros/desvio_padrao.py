# Etapa 1: calcular a média.
# Etapa 2: calcular o quadrado da distância entre cada ponto e a média.
# Etapa 3: somar os valores da Etapa 2.
# Etapa 4: dividir pelo número de pontos.
# Etapa 5: calcular a raiz quadrada.

# 2. Primeiro, precisamos de um conjunto de dados com o qual trabalhar. Vamos escolher algo 
# pequeno para que não sejamos sobrecarregados pelo número de pontos. Confira um bom: [6,2,3,1].
dados = [6, 2, 3, 1]

# 3. Nessa etapa, calculamos a média do conjunto de dados, que é representada pela variável N.
N = sum(dados) / len(dados)

# 4. Nessa etapa, calculamos a distância entre cada dado e a média (ou seja, os desvios), e o 
#quadrado de cada uma dessas distâncias. Por exemplo, o primeiro dado é 6, e a média é 3, então a 
#distância entre eles é de 3. O quadrado dessa distância é 9.
dist_quad = []
for v in dados:
    if (v-N) < 0:
        dist_quad.append(((v-N)*-1)**2)
        
    else:
        dist_quad.append((v-N)**2)
        

# 5. O símbolo ∑ significa "somatório", então nessa etapa vamos somar os quatro valores que 
#encontramos na etapa anterior.
sigma = sum(dist_quad)

# 6. Nessa etapa, dividimos o resultado obtido na etapa 3 pela variável N, que é o número de dados.
div = sigma / N

# 7. Agora, é só calcular a raiz quadrada da resposta da etapa anterior e terminamos. Preencha a 
#lacuna. Arredonde sua resposta para a segunda casa decimal
import math
raiz = math.sqrt(div)
dp = str(raiz)
print(f'\n--> O Desvio Padrão é: {dp[0:4]}')