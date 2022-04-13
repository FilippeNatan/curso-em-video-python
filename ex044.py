print('=-'*23)
print('{:^46}'.format('Casas Bahia'))
print('=-'*23)
precoProduto = float(input('Qual o valor do produto?\nR$ '))
condicaoPagamento = int(input('Escolha a condição de pagamento:'
                              '\n[1] À Vista: Dinheiro ou Cheque'
                              '\n[2] À Vista: Cartão'
                              '\n[3] Parcelado: Cartão 2x'
                              '\n[4] Parcelado: Cartão 3x ou mais\n'))
if condicaoPagamento == 1:
    valorPagamento = (precoProduto / 100) * 90
    print('O valor a ser pago é R$ {:.2f}'.format(valorPagamento))
elif condicaoPagamento == 2:
    valorPagamento = (precoProduto / 100) * 95
    print('O valor a ser pago é R$ {:.2f}'.format(valorPagamento))
elif condicaoPagamento == 3:
    valorPagamento = precoProduto
    print('O valor a ser pago é R$ {:.2f}'.format(valorPagamento))
elif condicaoPagamento == 4:
    valorPagamento = (precoProduto / 100) * 120
    print('O valor a ser pago é R$ {:.2f}'.format(valorPagamento))
else:
    print('Condição de pagamento inválida.')
