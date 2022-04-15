print('Todos os números pares de 1 a 50:')
for n in range(2, 51, 2): #melhor usar passo dois para consumir menos recurso
    if n % 2 == 0:
        print(n, end=' ')
