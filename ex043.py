peso = float(input('Informe seu peso:'))
altura = float(input('Informe sua altura:'))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('Você está bem magricela!')
elif imc >= 18.5 and imc < 25:
    print('Você está com um peso legal, mantenha o shape!')
elif imc >= 25 and imc < 30:
    print('Você está um pouco gordito!')
elif imc >= 30 and imc < 40:
    print('Você está baita!!!')
else:
    print('Você está extremamente gelatinoso!')