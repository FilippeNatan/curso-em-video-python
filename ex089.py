boletim = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2)/2
    boletim.append([nome, [nota1, nota2], media])
    querContinuar = str(input('Quer continuar? [S/N]'))[0].strip().upper()
    while querContinuar not in 'SN':
        querContinuar = str(input('Quer continuar? [S/N]')).strip().upper()
    if querContinuar == 'N':
        break
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)
for i, a in enumerate(boletim):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
    if i+1 == len(boletim):
        while True:
            consulta = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
            if consulta == 999:
                break
            print(f'Notas de {boletim[consulta][0]} foram {boletim[consulta][1]}')
print('Obrigado e volte sempre!')
