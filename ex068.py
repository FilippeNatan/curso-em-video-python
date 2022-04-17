from random import randint

print('|*|'*10)
print('{:^30}'.format('VAMOS JOGAR PAR OU IMPAR'))
print('|*|'*10)

vitorias = 0

while True:
    n = int(input('Diga um número: '))
    while n not in range(0,11):
        n = int(input('Diga um número: '))
    v = str(input('Escolha Par ou Ímpar: [P/I]')).upper().strip()
    while v not in 'PI':
        v = str(input('Escolha Par ou Ímpar: [P/I]')).upper().strip()
    c = randint(0, 10)
    s = n + c
    string = ''
    if s % 2 == 0:
        string = 'DEU PAR'
    else:
        string = 'DEU ÍMPAR'
    if s % 2 == 0 and v == 'P':
        vitorias += 1
        print(f'Você jogou {n} e o computador jogou {c}. Total de {s} {string}.')
        print('Você VENCEU!\n'
              'Vamos jogar novamente...')
    elif s % 2 != 0 and v == 'I':
        vitorias += 1
        print(f'Você jogou {n} e o computador jogou {c}. Total de {s} {string}.')
        print('Você VENCEU!\n'
              'Vamos jogar novamente...')
    else:
        print(f'Você jogou {n} e o computador jogou {c}. Total de {s} {string}.')
        print('Você PERDEU!\n'
              f'Obrigado por jogar... Você teve {vitorias} vitória(s)!')
        break
