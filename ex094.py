listaPessoas = []; pessoas = {}; totalIdade = 0; listaMulheres = []

while True:
    pessoas['nome'] = str(input('Nome: '))
    pessoas['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()
    while pessoas['sexo'] not in 'FM':
        pessoas['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()
    pessoas['idade'] = int(input('Idade: '))

    listaPessoas.append(pessoas.copy())

    querContinuar = str(input('Quer continuar? [S/N] ')).strip().upper()

    while querContinuar not in 'NS':
        querContinuar = str(input('Quer continuar? [S/N] ')).strip().upper()

    if querContinuar == 'N':
        break

print(listaPessoas)
print('-='*30)
print(f'- O grupo tem {len(listaPessoas)} pessoas.')
for n in range(0, len(listaPessoas)):
    totalIdade += listaPessoas[n]['idade']
    if listaPessoas[n]['sexo'] == 'F':
        listaMulheres.append(listaPessoas[n]['nome'])
mediaIdade = int(totalIdade / len(listaPessoas))
print(f'- A média de idade é de {mediaIdade} anos.')
print(f'- As mulheres cadastradas foram:', end=' ')
for n in range(0, len(listaMulheres)):
     print(f'{listaMulheres[n]}', end=' ')
print(f'\n- Lista das pessoas que estão acima da média de idade:')
for n in range(0, len(listaPessoas)):
    if listaPessoas[n]['idade'] > mediaIdade:
        print()
        print(f'nome = {listaPessoas[n]["nome"]}; sexo = {listaPessoas[n]["sexo"]}; idade = {listaPessoas[n]["idade"]}')
print('<< ENCERRADO >>')
