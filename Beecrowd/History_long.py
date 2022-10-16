inputo = []
while True:
    try:
        entrada = int(input())
    except:
        break 
    ativacao,x = 0,0
    while ativacao != 1:
        x += 1 
        if entrada <= (x*100) and entrada >= ((x*100)-99):
            century = x
            ativacao = 1
    inputo.append(century)
for v in inputo:
    print(v)