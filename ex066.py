n = c = s = 0

while n != 999:
    n = int(input('Informe um número: (Digite 999 para parar)'))
    if n == 999:
        break
    c += 1
    s += n

print(f'Foram digitados {c} números e o total da soma foi {s}.')
