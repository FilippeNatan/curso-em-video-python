from datetime import date

anoNascimento = int(input('Informe o ano do seu nascimento:\n'))
anoAtual =date.today().year

if (anoAtual - anoNascimento) < 18:
    print('Você ainda vai se alistar! Aproveite! Faltam {} anos!'.format(18 - (anoAtual - anoNascimento)))
elif (anoAtual - anoNascimento) == 18:
    print('Está na hora de se alistar. Corra!')
else:
    print('Você já se alistou, muito obrigado! Já passaram {} anos!'.format((anoAtual - anoNascimento) - 18))
