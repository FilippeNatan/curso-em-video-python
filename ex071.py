cedulas50 = 0; cedulas20 = 0; cedulas10 = 0; cedulas1 = 0

print('='*30)
print('{:^30}'.format('BANCO DO PEDREIRO'))
print('='*30)

valorDesejado = int(input('Qual o valor deseja sacar? R$ '))

if valorDesejado >= 50:
    while valorDesejado >= 50:
        valorDesejado -= 50
        cedulas50 += 1
if valorDesejado >= 20:
    while valorDesejado >= 20:
        valorDesejado -= 20
        cedulas20 += 1
if valorDesejado >= 10:
    while valorDesejado >= 10:
        valorDesejado -= 10
        cedulas10 += 1
if valorDesejado >= 1:
    while valorDesejado >= 1:
        valorDesejado -= 1
        cedulas1 += 1

if cedulas50 >= 1:
    print(f'RECEBA!!! {cedulas50} cédulas de R$ 50,00.')
if cedulas20 >= 1:
    print(f'RECEBA!!! {cedulas20} cédulas de R$ 20,00.')
if cedulas10 >= 1:
    print(f'RECEBA!!! {cedulas10} cédulas de R$ 10,00.')
if cedulas1 >= 1:
    print(f'RECEBA!!! {cedulas1} cédulas de R$ 1,00.')

print('O MELHOR DO MUNDO GRAÇAS A DEUS!!! SIIIIIUUUU')
