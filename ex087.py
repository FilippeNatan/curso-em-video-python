matriz = [[], [], [], [], [], [], [], [], []]; somaPares = 0;
somaTerceiraColuna = 0; maiorSegundaLinha = 0

for n in range(0, 3):
    v = int(input(f'Digite um valor para [0, {n}]: '))
    matriz[n].append(v)
    if n == 2:
        somaTerceiraColuna += v
    if v % 2 == 0:
        somaPares += v
for n in range(3, 6):
    v = int(input(f'Digite um valor para [1, {n-3}]: '))
    matriz[n].append(v)
    if v >= maiorSegundaLinha:
        maiorSegundaLinha = v
    if n == 5:
        somaTerceiraColuna += v
    if v % 2 == 0:
        somaPares += v
for n in range(6, 9):
    v = int(input(f'Digite um valor para [2, {n-6}]: '))
    matriz[n].append(v)
    if n == 8:
        somaTerceiraColuna += v
    if v % 2 == 0:
        somaPares += v
print('-='*30)
print(matriz[0], matriz[1], matriz[2])
print(matriz[3], matriz[4], matriz[5])
print(matriz[6], matriz[7], matriz[8])
print('-='*30)
print(f'A soma dos valores pares é {somaPares}.')
print(f'A soma dos valores da terceira coluna é {somaTerceiraColuna}.')
print(f'O maior valor da segunda linha é {maiorSegundaLinha}.')
