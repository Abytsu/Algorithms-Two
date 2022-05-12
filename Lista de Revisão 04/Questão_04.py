# Escreva um algoritmo que gere o números de 1000 a 1999 e escreva aqueles que dividido por 11 dão resto igual a 5.
a = 0
for v in range(1000,1999):
    if v % 11 == 5:
        print(f'> O valor {v} tem resto igual a 5 quando dividido por 11.')

    
