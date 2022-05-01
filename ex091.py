from random import randint

lista = []
jogadores = {}

print('Valores sorteados: ')
for n in range(1, 5):
    jogadores['jogador'] = n
    jogadores['dado'] = randint(1, 6)
    lista.append(jogadores.copy())
    print(f'Jogador {jogadores["jogador"]} tirou {jogadores["dado"]}')
for n in range(0, len(lista)):
    print(lista[n])
    