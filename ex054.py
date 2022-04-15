import datetime

date = datetime.date.today()
numPessoas = 7
contador = 1
numPessoasMaioridade = 0
numPessoasMinoridade = 0

print('Informe a data de nascimento de {} pessoas.'.format(numPessoas))
while(contador <= numPessoas):
    anoPessoa = int(input('Informe a o ano de nascimento de {}º pessoa: '.format(contador)))
    if(date.year - anoPessoa >= 21):
        numPessoasMaioridade+=1
    else:
        numPessoasMinoridade+=1
    contador+=1
print('O números de pessoas maiores de idade é {} e o número de menores é {}.'.format(numPessoasMaioridade, numPessoasMinoridade))
