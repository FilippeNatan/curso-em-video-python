from random import sample, shuffle
aluno1 = str(input('Informe o nome do primero aluno:'))
aluno2 = str(input('Informe o nome do segundo aluno:'))
aluno3 = str(input('Informe o nome do terceiro aluno:'))
aluno4 = str(input('Informe o nome do quarto aluno:'))
alunos = [aluno1, aluno2, aluno3, aluno4]
shuffle(alunos)
print('A order de apresentação será: {}'.format(alunos))
'''print('A order de apresentação será: {}'.format(sample(alunos, len(alunos))))'''
