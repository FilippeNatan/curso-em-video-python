nomeCidade = str(input('Digite o nome da sua cidade:'))
nomeCidadeSplitado = nomeCidade.upper().split()
print('O nome da cidade começa com SANTO? {}'.format('SANTO' in nomeCidadeSplitado[0]))
