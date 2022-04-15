num = int(input('Digite um número para saber sua tabuada: '))
print('A tabuada de {} é:'.format(num))
for incremento in range(1, 11):
    print('\n{} X {} = {}'.format(num, incremento, num * incremento))
