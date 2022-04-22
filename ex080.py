valores = []
for n in range(0, 5):
    valor = int(input('Digite um valor: '))
    if n == 0 or valor > valores[-1]:
        valores.append(valor)
        print('Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(valores):
            if n <= valores[pos]:
                valores.insert(pos, n)
                print(f'Adicionado a posição {pos} da lista')
                break
            pos += 1
print('-='*30)
print(f'Os valores digitados em ordem foram {valores}')
