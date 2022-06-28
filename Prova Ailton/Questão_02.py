A = []
##############

A.append(1)
A.append(0)
A.append(5)
A.insert(3, -2)
A.insert(4, -5)
A.insert(5, 7)

print(A)

###############

var_simple = int(A[0] + A[1] + A[5])
print(f'\n> A soma dos valores da posição 1, 2 e 6 é: {var_simple}\n')
############################################

A.insert(3, 100)
print(A)
##########################
print('\n')
for c in A:
    print(c)