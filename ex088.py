from random import randint
from time import sleep

jogo = []

print('-'*30)
print('{:^30}'.format('JOGA NA MEGA SENA'))
print('-'*30)

quantidadeDeJogos = int(input('Quantos jogos você quer que eu sorteie? '))

print(f'-=-=-= SORTEANDO {quantidadeDeJogos} JOGOS -=-=-=')

for p in range(0, quantidadeDeJogos):
    for n in range(0, 6):
        v = randint(1, 60)
        while v in jogo:
            v = randint(1, 60)
        jogo.append(v)
    sleep(0.5)
    jogo.sort()
    print(f'Jogo {p+1}: {jogo}')
    jogo.clear()
print('{:^30}'.format('BOA SORTE'))
