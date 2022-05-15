from random import randint

def sortear():
    print('Sorteando 5 valores da lista: ', end='')
    lista = []
    for n in range(0, 5):
        lista.append(randint(1, 10))
        print(lista[n], end=' ')
        n += 1
    print(('PRONTO!'))
    somarPares(lista)

def somarPares(lista):
    listaPares = []
    for n in range(0, len(lista)):
        if lista[n] % 2 == 0:
            listaPares.append(lista[n])
    print(f'Somando os valores pares de {lista}, temos {sum(listaPares)}')

sortear()
