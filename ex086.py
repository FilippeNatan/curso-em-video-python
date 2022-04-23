matriz = [[], [], [], [], [], [], [], [], []]
for n in range(0, 3):
    matriz[n].append(int(input(f'Digite um valor para [0, {n}]: ')))
for n in range(3, 6):
    matriz[n].append(int(input(f'Digite um valor para [1, {n-3}]: ')))
for n in range(6, 9):
    matriz[n].append(int(input(f'Digite um valor para [2, {n-6}]: ')))
print('-='*30)
print(matriz[0], matriz[1], matriz[2])
print(matriz[3], matriz[4], matriz[5])
print(matriz[6], matriz[7], matriz[8])
