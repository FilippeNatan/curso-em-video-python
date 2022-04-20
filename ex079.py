valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    varValidacao = valores[-1]
    if valores.count(varValidacao) > 1:
        valores.pop()
        print('Valor duplicado. Não vou adicionar...')
    else:
        print('Valor adicionado com sucesso: ')
    querContinuar=str(input('Quer continuar? [S/N]')).upper().strip()[0]
    while querContinuar not in 'SN':
        print('Opção inválida!')
        querContinuar = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if querContinuar == 'N':
        break
print('-='*30)
print('Voce digitou os valores ' ,end='')
print(sorted(valores))

