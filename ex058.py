from random import randint
from time import sleep

numComputador = randint(0, 10)
tentativas = 0

print('Tente me vencer! Pensei em um número entre 0 e 10...')
numUsuario = int(input('Tente adivinhar qual é:'))
while numComputador != numUsuario:
    print('PROCESSANDO...')
    sleep(1)
    tentativas += 1
    print('Você errou! Que pena!')
    if numUsuario < numComputador:
        print('É um número maior...')
    if numComputador < numUsuario:
        print('É um número menor...')
    numUsuario = int(input('Tente novamente: '))
print('PROCESSANDO...')
sleep(3)
tentativas += 1
print('Você acertou! Parabéns! O número era: {} e você precisou de {} tentativas.'.format(numComputador, tentativas))
