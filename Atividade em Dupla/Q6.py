# Escreva uma função que receba as dimensões de uma fotografia em centímetros (por exemplo 10 x 15 cm)
# e a densidade de píxeis da impressora (por exemplo 300 dpi), e retorne a resolução (por exemplo 2.1 mega
# píxeis) mínima necessária para imprimir aquela foto. A densidade de píxeis da impressora diz quantos
# píxeis são impressos a cada polegada. Por exemplo: 300 dpi (dots per inch, ou pontos por polegada)
# significa que em uma polegada em linha reta da imagem há 300 píxeis.  
def impressora(dimensaoLargura, dimensaoAltura, dpi):
    imagem = dimensaoLargura * dimensaoAltura
    resolucao = imagem * dpi
    return print(f'Píxeis necessários para a impressão: {resolucao} px\nOu {resolucao/(10**6)} MP\n')
impressora(10,15,300)
impressora(1100,660,200)