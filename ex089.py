boletim = []; contador = 0; numeroAluno = 0

while True:
    nome = str(input('Nome: '))
    nota1 = int(input('Nota 1: '))
    nota2 = int(input('Nota 2: '))
    boletim.append([numeroAluno])
    boletim.append([nome])
    boletim.append([nota1, nota2])
    numeroAluno += 1
    querContinuar = str(input('Quer continuar? [S/N]'))[0].strip().upper()
    while querContinuar not in 'SN':
        querContinuar = str(input('Quer continuar? [S/N]')).strip().upper()
    if querContinuar == 'N':
        break
print('Nº NOME            MÉDIA')
print('-'*30)

for n in range(0,len(boletim)):
    if contador != 2:
        print(boletim[n][0], end=' ')
        contador += 1
    else:
        print(f'{boletim[n][0]}\n')
        contador = 0