valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    querContinuar=str(input('Quer continuar: [S/N]')).upper().strip()[0]
    if querContinuar not in 'SN':
        print('Opção inválida!')
        querContinuar = str(input('Quer continuar: [S/N]'))
    if querContinuar == 'N':
        break
print('-='*30)
print(f'Você digitou {len(valores)} elementos.')
print(f'Os valores em ordem decrescente são {sorted(valores, reverse=True)}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')
