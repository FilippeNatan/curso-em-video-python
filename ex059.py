primeiroNumero = int(input('Digite o primeiro número: '))
segundoNumero = int(input('Digite o segundo número: '))
comando = 0
while comando != 5:
    comando = int(input('Informe que operação deseja fazer:\n'
          '[1] SOMAR\n'
          '[2] MULTIPLICAR\n'
          '[3] MAIOR\n'
          '[4] NOVOS NÚMEROS\n'
          '[5] SAIR\n'))
    if comando == 1:
        soma = primeiroNumero + segundoNumero
        print('A soma de {} e {} é {}'.format(primeiroNumero, segundoNumero, soma))
    if comando == 2:
        multiplicacao = primeiroNumero * segundoNumero
        print('A multiplicação de {} e {} é {}'.format(primeiroNumero, segundoNumero, multiplicacao))
    if comando == 3:
        if(primeiroNumero > segundoNumero):
            print('O maior número é {}'.format(primeiroNumero))
        if(segundoNumero > primeiroNumero):
            print('O maior número é {}'.format(segundoNumero))
        if(primeiroNumero == segundoNumero):
            print('{} é igual a {}'.format(primeiroNumero, segundoNumero))
    if comando == 4:
        primeiroNumero = int(input('Informe o primeiro número novo: '))
        segundoNumero = int(input('Informe o segundo número novo: '))
print('FIM!')