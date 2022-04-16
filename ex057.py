sexo = ''
while sexo == '':
    sexo = str(input('Informe o seu sexo: [M/F]')).strip().upper()[0]
    if sexo not in 'MFmf':
        sexo = ''
        print('Valor inválido, digite M ou F.')
print('Sexo {} registrado com sucesso!'.format(sexo))
