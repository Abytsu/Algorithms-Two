N = int(input())
moeda = str(input())
moeda = moeda[0].upper()
for v in range(N):
    mov = int(input())
    if mov == 1:
        if moeda == 'A':
            moeda = 'B'
        elif moeda == 'B':
            moeda = 'A'
    elif mov == 2:
        if moeda == 'B':
            moeda = 'C'
        elif moeda == 'C':
            moeda = 'B'
    elif mov == 3:
        if moeda == 'A':
            moeda = 'C'
        elif moeda == 'C':
            moeda = 'A'
print(moeda)