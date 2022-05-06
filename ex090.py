alunos = {}
alunos['nome'] = str(input('Nome: '))
alunos['média'] = float(input(f'Qual a média de {alunos["nome"]}? '))
if alunos['média'] > 6:
    alunos['situação'] = 'Aprovado'
    print(f'Situação é igual {alunos["situação"]}')
else:
    alunos['situação'] = 'Reprovado'
    print(f'Situação é igual a {alunos["situação"]}')
print(alunos)
