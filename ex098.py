from time import sleep

def traço():
    print('=-='*10)


def contador(inicio, fim, passo):
    traço()
    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio < fim:
        while inicio <= fim:
            sleep(0.3)
            print(inicio, end=' ')
            inicio += passo
    else:
        while inicio >= fim:
            sleep(0.3)
            print(inicio, end=' ')
            inicio -= passo
    print(' FIM!')  # tive que fazer isso pra pular linha =P
    traço()

contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
