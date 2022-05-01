import datetime
pessoa = {}
pessoa['nome'] = str(input('Nome: '))
anoNascimento = int(input('Ano de Nascimento: '))
pessoa['idade'] = datetime.datetime.now().year - anoNascimento
pessoa['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if pessoa['ctps'] == 0:
    print('-=-'*10)
    print(pessoa)
else:
    pessoa['anoContratacao'] = int(input('Ano de contratação: '))
    pessoa['salário'] = float(input('Salário: '))
    anoAposentadoria = pessoa['anoContratacao']+35
    pessoa['aposentadoria'] = anoAposentadoria - anoNascimento
    print('-=-' * 10)
    print(pessoa)
for i, v in pessoa.items():
    print(f'{[i][0]} tem o valor {[v][0]}')
