v1, v2, c1, c2, t = [],[],0,0,0

for l1 in range(5):
    v1.append(int(input(f'Digite o valor da posição {l1+1} do primeiro vetor: ')))
print('\n')
for l2 in range(5):
    v2.append(int(input(f'Digite o valor da posição {l2+1} do segundo vetor: ')))

for check in v1:
    c1 +=1 
    for check2 in v2:
        if v2.index(check2) == 0:
           c2 = 0 
        c2 += 1
        if check2 == check:
            print(f'O valor {check2} é comum em ambas as listas. Ele está na posição {c1} na primeira lista e na posição {c2} na segunda lista.')
            t = 1
if t == 0:
    print('\nNão tem valores iguais nas listas.')


