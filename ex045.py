from random import randint
from time import sleep

print('=-'*45)
print('{:^90}'.format('JOKENPÔ'))
print('=-'*45)

escolhaUsuario = int(input('Escolha Pedra, Papel ou Tesoura:'
                           '\n[1] PEDRA'
                           '\n[2] PAPEL'
                           '\n[3] TESOURA\n'))

escolhaComputador = randint(1, 3)

if escolhaUsuario == 1 and escolhaComputador == 1:
    sleep(3)
    print('Escolhi PEDRA. Empatamos!')
elif escolhaUsuario == 1 and escolhaComputador == 2:
    sleep(3)
    print('Escolhi PAPEL. PAPEL embrulha PEDRA. Você perdeu!')
elif escolhaUsuario == 1 and escolhaComputador == 3:
    sleep(3)
    print('Escolhi TESOURA. PEDRA quebra TESOURA. Você ganhou!')
elif escolhaUsuario == 2 and escolhaComputador == 1:
    sleep(3)
    print('Escolhi PEDRA. PAPEL embrulha PEDRA. Você ganhou!')
elif escolhaUsuario == 2 and escolhaComputador == 2:
    sleep(3)
    print('Escolhi PAPEL. Empatamos!')
elif escolhaUsuario == 2 and escolhaComputador == 3:
    sleep(3)
    print('Escolhi TESOURA. TESOURA corta PAPEL. Você perdeu!')
elif escolhaUsuario == 3 and escolhaComputador == 1:
    sleep(3)
    print('Escolhi PEDRA. PEDRA quebra TESOURA. Você perdeu!')
elif escolhaUsuario == 3 and escolhaComputador == 2:
    sleep(3)
    print('Escolhi PAPEL. TESOURA corta PAPEL. Você ganhou!')
elif escolhaUsuario == 3 and escolhaComputador == 3:
    sleep(3)
    print('Escolhi TESOURA. Empatamos!')
else:
    print('Opção inválida!')