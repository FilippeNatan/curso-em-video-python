nome = str(input('Informe seu nome completo: ')).strip()
nomeSplitado = nome.split()
print('O primeiro nome é {} e o último nome é {}'.format(nomeSplitado[0], nomeSplitado[-1]))
