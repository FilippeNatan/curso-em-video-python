from random import choice
nome1 = str(input('Informe o nome do primeiro aluno:'))
nome2 = str(input('Informe o nome do segundo aluno:'))
nome3 = str(input('Informe o nome do terceiro aluno:'))
nome4 = str(input('Informe o nome do quarto aluno:'))
pessoas = [nome1, nome2, nome3, nome4]
sorteio = choice(pessoas)
print('O aluno sorteado é {}.'.format(sorteio))
