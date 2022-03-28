from random import randint
from time import sleep

numComputador = randint(0, 5)
print('Tente me vencer! Pensei em um número entre 0 e 5...')
numUsuario = int(input('Tente adivinhar qual é:'))
print('PROCESSANDO...')
sleep(3)
if numComputador == numUsuario:
    print('Você acertou! Parabéns! O número era: {}'.format(numComputador))
else:
    print('Você errou! Que pena! O número era: {}'.format(numComputador))
