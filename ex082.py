valores = []; valoresPares = []; valoresImpares = []
while True:
    valores.append(int(input('Digite um número: ')))
    querContinuar = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    while querContinuar not in 'NS':
        print ('Valor inválido!', end=' ')
        querContinuar = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if querContinuar == 'N':
        for n in valores:
            if n % 2 == 0:
                valoresPares.append(n)
            else:
                valoresImpares.append(n)
        break
print(f'A lista completa é {valores}')
print(f'A lista de pares é {valoresPares}')
print(f'A lista de ímpares é {valoresImpares}')
