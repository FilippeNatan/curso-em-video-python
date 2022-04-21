valores = []
for n in range(0, 5):
    valor = int(input('Digite um valor: '))
    if n == 0:
        valores.append(valor)
        print('Adicionado ao final da lista')
    else:
        for i, v in enumerate(valores):
            if valor > valores(v):
                valores.append((valor))
            elif valor < valores(v):
                valores.insert(i, valor)
print(valores)
