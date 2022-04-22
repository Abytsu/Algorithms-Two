# Desenvolver um algoritmo que efetue a soma de todos os números ímpares e que se
# encontram no conjunto dos números de 1 até 500.
originum,odd = 0,0
while originum < 500:
    if originum % 2 == 1:
        odd = originum + odd 
    originum += 1
print('A soma dos números impáres de 1 a 500 é: {0}'.format(odd))