from time import sleep

nomes = []; idades = []; sexo = []; numPessoa = 4; homemMaiorIdade = 0; homemMaiorIdadeNome = 'Ninguém'; mulheresMenos20Anos = 0

for contador in range(numPessoa):

    nomes.append(input('Informe o nome da {}º pessoa: '.format(contador + 1)))
    idades.append(int(input('Informe a idade da {}º pessoa: '.format(contador + 1))))
    sexo.append(input('Informe o sexo da {}º pessoa(M ou F): '.format(contador + 1)))

    if (sexo[contador] in 'Mm' and idades[contador] > homemMaiorIdade):
        homemMaiorIdade = idades[contador]
        homemMaiorIdadeNome = nomes[contador]

    if(sexo[contador] in 'Ff' and idades[contador] < 20):
        mulheresMenos20Anos+=1

somaIdades = sum(idades) / numPessoa
print('\nCALCULANDO...')
sleep(1)
print('\nA média de todas as idades é {} anos.'.format(somaIdades))
print('O homem mais velho é {} e ele tem {} anos.'.format(homemMaiorIdadeNome, homemMaiorIdade))
print('O total de mulheres com menos de 20 anos é {} mulher(es).'.format(mulheresMenos20Anos))
