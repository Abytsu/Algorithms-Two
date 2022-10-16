# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três
# argumentos através de uma função. Seu script também deve fornecer a média dos três números, através de
# uma segunda função que chama a primeira
def func1(x,y,z):
    return x+y+z
def media1(x,y,z):
    return func1(x,y,z)/3
print(func1(4,4,8))
print(media1(5,7,9))
