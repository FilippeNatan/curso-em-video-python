print('A soma de todos os números ímpares entre 1 e 500, múltiplos de 3:')
soma = 0
cont = 0
for n in range(3, 501, 2):
    if(n % 3 == 0):
        cont +=1
        soma += n
        print(n, end=' ')
print('\n\nO total da soma é: {}'.format(soma))
print('\nO total de valores somados é {}.'.format(cont))