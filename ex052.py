num = int(input('Informe um número para saber se é um número primo:'))
#Solução do professor Guanabara
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[m0 número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO')
#Minha primeira solução, muito ruim
#if(num % 2 != 0 and num % 3 != 0 and num % 5 != 0 or num == 5):
#    print('O número é primo!')
#else:
#    print('O número não é primo!')
