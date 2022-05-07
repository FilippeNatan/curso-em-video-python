dadosJogador = {}; listaGols = []; listaJogadores = []

while True:
    dadosJogador['nome'] = str(input('Nome do Jogador: '))
    dadosJogador['partidas'] = int(input(f'Quantas partidas {dadosJogador["nome"]} jogou? '))
    for n in range(0, dadosJogador['partidas']):
        listaGols.append(int(input(f'Quantos gols na partida {n+1}? ')))
    dadosJogador['gols'] = listaGols[:]
    listaJogadores.append(dadosJogador.copy())
    listaGols.clear()
    querContinuar = str(input('Quer continuar? [S/N] ')).upper().strip()
    if querContinuar not in 'NS':
        print('Opção inválida!')
        querContinuar = str(input('Quer continuar? [S/N] ')).upper().strip()
    if querContinuar == 'N':
        break
print(dadosJogador)
print('=-='*15)
print(f'{"cod":<5}{"nome":<10}{"gols":15}{"total":<30}')
print('-'*45)
for i, v in enumerate(listaJogadores):
    print(f'{i:<5}{v["nome"]:<10}{v["gols"]}{sum(v["gols"]):>10}')
while True:
    consulta = int(input('Mostrar dados de qual jogador? '))
    if consulta == 999:
        break
    if consulta < 0 or consulta > len(listaJogadores)-1:
        print('Erro! Número de jogador inválido.')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {listaJogadores[consulta]["nome"]}:')
        for h, n in enumerate(listaJogadores[consulta]['gols']):
            print(f'Na partida {h+1}, fez {n} gols.')
