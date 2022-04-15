from datetime import date

date = date.today()
numPessoas = 7
contador = 1
numPessoasMaioridade = 0
numPessoasMinoridade = 0

print('Informe a data de nascimento de {} pessoas.'.format(numPessoas))
for pessoa in range(0, numPessoas):
    anoPessoa = int(input('Informe a o ano de nascimento de {}ª pessoa: '.format(contador)))
    if(date.year - anoPessoa >= 21):
        numPessoasMaioridade+=1
    else:
        numPessoasMinoridade+=1
    contador+=1
print('O números de pessoas maiores de idade é {} e o número de menores é {}.'.format(numPessoasMaioridade, numPessoasMinoridade))
