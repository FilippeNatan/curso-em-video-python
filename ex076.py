tuplaProdutos = ('Pão', 10, 'Leite', 8, 'Ovos', 15, 'Frango', 13, 'Biscoito', 4)
print('-'*40)
print('{:^40}'.format('LISTA DE PREÇOS'))
print('-'*40)
for num in tuplaProdutos:
    if tuplaProdutos.index(num) % 2 == 0:
        print(f'{tuplaProdutos[tuplaProdutos.index(num)]:.<30}R$', end=' ')
    else:
        print(f'{tuplaProdutos[tuplaProdutos.index(num)]:>7.2f}')
