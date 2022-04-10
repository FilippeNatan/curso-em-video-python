from datetime import date

anoNascimento = int(input('Informe seu ano de nascimento:\n'))
anoAtual = date.today().year
idade = anoAtual - anoNascimento

print('O atleta tem {} anos:'.format(idade))
if idade <= 9:
    print('O atleta é MIRIM.')
elif idade <= 14:
    print('O atleta é INFANTIL.')
elif idade <= 19:
    print('O atleta é JUNIOR.')
elif idade <= 20:
    print('O atleta é SÊNIOR.')
else:
    print('O atleta é MASTER.')
