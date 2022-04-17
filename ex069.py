continuar = 'S'; contadorMaior18 = 0; contadorHomens = 0; contadorMulheresMenorDe20 = 0

while True:
    idade = int(input('Informe a idade da pessoa: '))
    sexo = str(input('Informe o sexo da pessoa: [M/F]')).upper().strip()[0]
    while sexo not in 'MFmf':
        print('Sexo inválido!')
        sexo = str(input('Informe o sexo da pessoa: [M/F]')).upper().strip()[0]
    if idade >= 18:
        contadorMaior18 += 1
    if sexo in 'Mm':
        contadorHomens += 1
    if sexo in 'Ff' and idade > 20:
        contadorMulheresMenorDe20 += 1
    continuar = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    while continuar not in 'SNsn':
        print('Opção inválida!')
        continuar = str(input('Quer continuar [S/N]')).upper().strip()[0]
    if continuar in 'Nn':
        break
print(f'Foram cadastrada(s) {contadorMaior18} pessoa(s) maiores de 18 anos.\n'
      f'Foram cadastrado(s) {contadorHomens} homens.\n'
      f'Foram cadastrada(s) {contadorMulheresMenorDe20} mulheres com mais de 20 anos.')