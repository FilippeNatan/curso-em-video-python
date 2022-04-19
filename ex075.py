primeiraVez = True; boolPares = False
tuplaInput = (int(input('Digite o primeiro valor: ')), int(input('Digite o segundo valor: ')),
              int(input('Digite o terceiro valor: ')), int(input('Digite o quarto valor: ')))
print(f'Você digitou {tuplaInput}')
print(f'O valor 9 apareceu {tuplaInput.count(9)} vez(es)')
if tuplaInput.count(3) >= 1:
    print(f'O primeiro valor 3 foi digitado na {tuplaInput.index(3)+1}ª posição')
else:
    print('O número 3 não foi digitado.')
for num in tuplaInput:
    if num % 2 == 0:
        boolPares = True
        if primeiraVez == True:
            primeiraVez = False
            print('Os valores pares digitados foram: ', end = '')
        print(num, end = ' ')
if boolPares == False:
    print('Não foram digitados números pares!')
