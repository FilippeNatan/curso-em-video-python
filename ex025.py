nome = str(input('Insira seu nome completo: '))
nomeSplitado = nome.upper().split()
print('Tem "Silva" no nome? {}'.format('SILVA' in nomeSplitado))
