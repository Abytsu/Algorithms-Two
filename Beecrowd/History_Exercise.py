while True:
    entrada = int(input())
    ativacao,x = 0,0
    while ativacao != 1:
        x += 1 
        if entrada <= (x*100) and entrada >= ((x*100)-99):
            century = x
            ativacao = 1
    print(century)