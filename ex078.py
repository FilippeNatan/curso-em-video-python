valores = []; listaMaiores = [0]; listaMenores = [0];
posicoesMaiores = []; posicoesMenores = []; primeiraVez = True

for n in range(0, 5):
    valores.append(int(input(f'Digite o {n+1}º valor: ')))
    if valores[n] == max(listaMaiores):
        listaMaiores.append(valores[n])
    if valores[n] > max(listaMaiores):
        del listaMaiores[0:]
        listaMaiores.append(valores[n])
    if valores[n] == min(listaMenores):
        listaMenores.append((valores[n]))
    if valores[n] < min(listaMenores) or primeiraVez == True:
        primeiraVez = False
        del listaMenores[0:]
        listaMenores.append(valores[n])
for i, n in enumerate(valores):
    if n in listaMaiores:
        posicoesMaiores.append(i)
for i, n in enumerate(valores):
    if n in listaMenores:
        posicoesMenores.append(i)
print(f'Você digitou {valores}')
print(f'O maior valor digitado foi: {max(valores)} nas posições ', end='')
for n in posicoesMaiores:
    print(f'{n}...', end=' ')
print(f'\nO menor valor digitado foi: {min(valores)} nas posições ', end='')
for n in posicoesMenores:
    print(f'{n}...', end=' ')