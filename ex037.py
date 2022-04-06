numeroDesejado = int(input('Informe o número que deseja converter:\n'))
baseConversao = int(input('Informe qual a base de conversão desejada:'
                          '\n[1] Binário'
                          '\n[2] Octal'
                          '\n[3] Hexadecimal\n'))
if baseConversao == 1:
    print('O número {} convertido para Binário é: {}'.format(numeroDesejado, bin(numeroDesejado)[2:]))
elif baseConversao == 2:
    print('O número {} convertido para Octal é: {}'.format(numeroDesejado, oct(numeroDesejado)[2:]))
elif baseConversao == 3:
    print('O número {} convertido para Hexadecimal é: {}'.format(numeroDesejado, hex(numeroDesejado)[2:]))
else:
    print('A base de conversão é inválida!')
