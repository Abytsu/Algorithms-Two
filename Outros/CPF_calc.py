CPF = str(input('Digite o CPF (com "." e "-"): '))
mult,store = 0,0
vezes = 0
var = 0
if len(CPF) > 14:
    exit(print('CPF  invalído'))
vezes = 10
for v in range(0,11):
    var = v
    if CPF[var] == '.' or CPF[var] == '-':
        mult = mult
    else:
        store = mult + store
        mult = (int(CPF[var]) * vezes)
        vezes -= 1 
        if v == 10:
            store = mult + store
resultado = store
calc1 = resultado * 10 % 11
if calc1 == 10:
    calc1 = 0
vezes,var,mult,store = 11,0,0,0
for v in range(0,13):
    var = v
    if CPF[var] == '.' or CPF[var] == '-':
        mult = mult
    else:
        store = mult + store
        mult = (int(CPF[var]) * vezes)
        vezes -= 1 
        if v == 12:
            store = mult + store
resultado = store
calc2 = resultado * 10 % 11
if calc2 == 10:
    calc2 = 0
if calc1 == int(CPF[12]) and calc2 == int(CPF[13]):
    print('É um CPF válido.')
else:
    print('Não é um CPF válido.')
