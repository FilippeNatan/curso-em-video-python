valores = [[], []]
for n in range(1, 8):
    v = (int(input(f'Digite o {n}º valor: ')))
    if v % 2 == 0:
        valores[0].append(v)
    else:
        valores[1].append(v)
print(f'Os valores pares digitados em ordem crescente foram: {sorted(valores[0])}.')
print(f'Os valores ímpares digitados em ordem crescente foram: {sorted(valores[1])}.')
