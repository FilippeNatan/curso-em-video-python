numero = 0
soma = 0
quantidadeDigitada = 0

while numero != 999:
    numero = int(input('Informe um número: (Digite 999 para terminar)\n'))
    if numero != 999:
        soma = soma + numero
        quantidadeDigitada += 1

print('Foram digitados {} números e a soma é {}'.format(quantidadeDigitada, soma))
