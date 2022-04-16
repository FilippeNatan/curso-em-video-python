maiorNumero = 0; menorNumero = 0; querContinuar = 'S'; contador = 0; soma = 0; primeiraVez = True

while querContinuar not in 'Nn':
    numero = int(input('Informe um número: '))
    if primeiraVez == True:
        primeiraVez = False
        maiorNumero = menorNumero = numero
    if numero > maiorNumero:
        maiorNumero = numero
    if numero < maiorNumero:
        menorNumero = numero
    contador += 1
    soma += numero
    media = soma / contador
    querContinuar = input('Quer continuar? [S/N]: ')
    if querContinuar not in 'SNsn':
        print('Opção inválida!')
        querContinuar = input('Quer continuar? [S/N]: ')

print('A média dos números digitados foi {}.\n'
      'A soma dos números digitados foi {}.\n'
      'O maior número digitado foi {}\n'
      'O menor número digitado foi {}'.format(media, soma, maiorNumero, menorNumero))
