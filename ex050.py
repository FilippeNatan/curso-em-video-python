print('Informe 6 números para saber a soma dos pares:')
soma = 0
for passo in range(1, 7):
    num = int(input('Informe o {}º número: '.format(passo)))
    if num % 2 == 0:
        soma += num
print('A soma dos número(s) PARES é: {}'.format(soma))
