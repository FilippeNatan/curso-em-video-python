from time import sleep

print('=-'*19)
print('{:^40}'.format('Minha Casa, Minha Dívida!'))
print('=-'*19)

valorImovel = float(input('Qual o valor do imóvel?\nR$ '))
valorSalario = float(input('Qual o valor do seu salário?\nR$ '))
anosPagar = int(input('Em quantos anos pretente pagar?\n'))

valorPrestacao = valorImovel / (anosPagar * 12)

valorMinimo = (valorSalario / 100) * 30

if valorPrestacao <= valorMinimo:
    sleep(3)
    print('O valor da prestação será de R$ {:.2f}'
          '\nSeu empréstimo foi \033[32mAPROVADO\033[m!'.format(valorPrestacao))
else:
    sleep(3)
    print('O valor da prestação é muito alto. R$ {:.2f}.'
          '\nSeu empréstimo foi \033[31mNEGADO\033[m!'.format(valorPrestacao))
