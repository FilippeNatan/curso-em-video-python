sexo = ''
while sexo == '':
    sexo = input('Informe o seu sexo: ')
    if sexo not in 'MFmf':
        sexo = ''
        print('Valor inválido, digite M ou F.')
print('FIM!')
