tuplaPalavras = ('Vodka', 'Gin', 'Cerveja', 'Vinho', 'Leite')

for num in range(0, len(tuplaPalavras)-1):
    palavra = tuplaPalavras[num].upper()
    print(f'\nNa palavra {palavra} temos essas vogais: ', end=' ')
    for num in range(0, len(palavra)):
        letra = palavra[num]
        if letra in 'AEIOU':
            print(letra, end=' ')
