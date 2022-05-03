pessoas = []; dado=[]; maiorPeso = 0; maiorPesoPessoa = [];
menorPeso = 0; menorPesoPessoa = []

while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    pessoas.append(dado[:])
    dado.clear()
    resp = str(input('Quer continuar? [S/N]')).upper().strip()
    if resp not in 'SN':
        print('Resposta inválida! ', end='')
        resp = str(input('Quer continuar? [S/N]')).upper().strip()
    if resp == 'N':
        for n in range(0, len(pessoas)):
            if n == 0 or pessoas[n][n] > maiorPeso:
                maiorPeso = pessoas[n][1]
                maiorPesoPessoa.clear()
                maiorPesoPessoa.append(pessoas[n])
            if n == 0 or pessoas[n][n] < menorPeso:
                menorPeso = pessoas[n][1]
                menorPesoPessoa.clear()
                menorPesoPessoa.append(pessoas[n])
            if pessoas[n][n] == maiorPeso:
                maiorPesoPessoa.append(pessoas[n])
            if pessoas[n][n] == menorPeso:
                menorPesoPessoa.append(pessoas[n])
        break
print('-='*30)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maiorPeso} Kg. Peso de {maiorPesoPessoa[0]}')
print(f'O menor peso foi de {menorPeso} Kg. Peso de {menorPesoPessoa[0]}')
