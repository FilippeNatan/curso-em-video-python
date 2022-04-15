primeiroTermo = int(input('Informe o primeiro termo de uma progressão aritimética: '))
razao = int(input('Informe a razão desta progressão: '))
termoRazao = primeiroTermo
for primeiroTermo in range(primeiroTermo, 10):
    print(termoRazao, end='->')
    termoRazao = termoRazao + razao
print('Acabou')