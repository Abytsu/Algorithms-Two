# Duas palavras são anagramas se você puder soletrar uma rearranjando as letras da outra.
# Escreva uma função chamada (is_anagram) que tome duas string e retorne ("Sim") se forem
# anagramas ou ("Não") caso contrário.
def is_anagram(palavra1, palavra2):
    palavra1 = ''.join(sorted(palavra1))
    palavra2 = ''.join(sorted(palavra2))
    if palavra1 == palavra2:
        print('Sim')
    else:
        print('Não')
is_anagram('amor','roma')
is_anagram('pedra','adrep')
is_anagram('nothing','love')
is_anagram('gaman','manga')
