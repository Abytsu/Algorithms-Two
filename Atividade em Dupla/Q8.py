# Tanto cadeias DNA quanto RNA são sequências de nucleotídeos. O DNA é formado por:
# adenina (A), citosina (C), guanina (G) e timina (T). E o RNA é formado por: 
# adenina (A), citosina (C), guanina (G) e uracila (U). Dada uma cadeia de DNA,
# o RNA transcrito é formado substituindo um nucleotídeo pelo seu complemento:
# G > C
# C > G
# T > A
# A > U    
# Implemente uma função que receba uma cadeia de DNA como string e retorno a o RNA complementar.
def transfusor(DNA):
    datapack = DNA
    DNA = DNA.upper()
    DNA = DNA.replace('A', 'u')
    DNA = DNA.replace('T', 'a')
    DNA = DNA.replace('G', 'c')
    DNA = DNA.replace('C', 'g')
    DNA = DNA.upper()
    return print(f'RNA complementar do DNA {datapack} é: {DNA}')
transfusor('ATGC')
transfusor('GTCA')
transfusor('GTAC')