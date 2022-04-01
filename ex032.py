anoUsuario = int(input('Informe um ano para saber se é BISSEXTO:'))
if (anoUsuario % 4) == 0:
    if (anoUsuario % 100) == 0:
        if(anoUsuario % 400) == 0:
            print('O ano é BISSEXTO!')
        else:
            print('O ano não é BISSEXTO!')
    else:
        print('O ano é BISSEXTO!')
else:
    print('O ano não é BISSEXTO!')
