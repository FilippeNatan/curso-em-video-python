primeiroTermo = int(input('Informe o primeiro termo de uma progressão aritimética: '))
razao = int(input('Informe a razão desta progressão: '))
termoRazao = primeiroTermo
termos = 10

while termos > 0:
    print(termoRazao, end='->')
    termoRazao = termoRazao + razao
    termos -= 1

print('Acabou')

