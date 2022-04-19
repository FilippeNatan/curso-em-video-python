from random import randint

tuplaNumerosAleatorios = (randint(0, 99), randint(0, 99), randint(0, 99),
                          randint(0, 99), randint(0, 99))

print(f'Sorteio de Números: {tuplaNumerosAleatorios}')

print(f'O maior número foi: {max(tuplaNumerosAleatorios)}')

print(f'O menor número foi: {min(tuplaNumerosAleatorios)}')
