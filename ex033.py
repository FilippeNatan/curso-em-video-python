primeiroNumero = float(input('Informe o primeiro número:\n'))
segundoNumero = float(input('Informe o segundo número:\n'))
terceiroNumero = float(input('Informe o terceiro número\n'))

maiorNumero = 0
menorNumero = 0

if primeiroNumero >= segundoNumero:
    maiorNumero = primeiroNumero
    menorNumero = segundoNumero
else:
    maiorNumero = segundoNumero
    menorNumero = primeiroNumero

if terceiroNumero >= maiorNumero:
    maiorNumero = terceiroNumero

if terceiroNumero < menorNumero:
    menorNumero = terceiroNumero

print('O maior número é {:.2f} e o menor número é {:.2f}'.format(maiorNumero, menorNumero))
