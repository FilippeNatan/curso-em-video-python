from random import randint

def maior(*num):
    maior = 0
    print('-' * 30)
    print('Analisando os valores passados...')
    for n in range(0, len(num)):
        print(num[n], end=' ')
        if num[n] > maior or n == 0:
            maior = num[n]
    if n == 0:
        print(f'\nForam informados {n} valores ao todo')
    else:
        print(f'\nForam informados {n+1} valores ao todo')
    print(f'O maior valor informado foi o {maior}')
maior(randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10) ,randint(0, 10) ,randint(0, 10))
maior(randint(0, 10), randint(0, 10), randint(0, 10))
maior(randint(0, 10), randint(0, 10))
maior(randint(0, 10))
maior(randint(0, 0))