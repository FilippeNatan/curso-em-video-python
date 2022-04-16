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
        print('A soma de {} + {} = {}'.format(primeiroNumero, segundoNumero, soma))
    elif comando == 2:
        multiplicacao = primeiroNumero * segundoNumero
        print('A multiplicação de {} x {} = {}'.format(primeiroNumero, segundoNumero, multiplicacao))
    elif comando == 3:
        if(primeiroNumero > segundoNumero):
            print('{} é maior que {}'.format(primeiroNumero, segundoNumero))
        elif(segundoNumero > primeiroNumero):
            print('{} é maior que {}'.format(segundoNumero, primeiroNumero))
        else:
            print('{} é igual a {}'.format(primeiroNumero, segundoNumero))
    elif comando == 4:
        primeiroNumero = int(input('Informe o primeiro número novo: '))
        segundoNumero = int(input('Informe o segundo número novo: '))
    if comando not in (1,2,3,4,5):
        print('Comando inválido, utilize um comando da lista...')
print('FIM!')