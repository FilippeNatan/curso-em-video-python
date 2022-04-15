numero = int(input('Informe um número que deseja saber o fatorial: '))
retornoNumero = numero
fatorial = numero

while numero != 1:
    multi = fatorial * (numero - 1)
    fatorial = multi
    numero -= 1

print('O resultado de {}! é {}'.format(retornoNumero, fatorial))