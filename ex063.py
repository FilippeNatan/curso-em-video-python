numero = int(input('Informe o número de termos que deseja ver da Sequência de Fibonacci: \n'))
primeiroNumero = 0
segundoNumero = 1
primeiraVez = True

while numero > 0:
    if primeiraVez == True:
        print(primeiroNumero, end='->')
        primeiraVez = False
    else:
        soma = primeiroNumero + segundoNumero
        print(soma, end='->')
        primeiroNumero = segundoNumero
        segundoNumero = soma
    numero -= 1
print('Acabou!')