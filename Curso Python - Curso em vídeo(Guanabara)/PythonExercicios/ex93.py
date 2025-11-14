from math import ceil

print()
print(f'{'QUALIFICAÇÃO DOS JOGADORES NO BRASILEIRÃO':^50} ')
print('-'*50)

print('insira os dados correspondentes: ')
print()
jogador = {
    'Nome' : input('Nome do jogador: ').capitalize(),
    'Time' : input('Por qual time o jogador é contratado no momento: ').capitalize()
}

q_jogos = int(input('Quantos jogos jogou até o momento: '))

gools = []
for c in range(0,q_jogos):
    g = int(input(f'Quantos gools foram feitos na {c+1}° partida: '))
    gools.append(g)

jogador['Quantidade de jogos'] = q_jogos
jogador['Gools/partida'] = gools
jogador['Total de gools'] = sum(gools)
jogador['Média de gools/partida'] = sum(gools)/q_jogos

print('-'*50)
print('Dados do jogador: ')
print('-'*50)

for k,v in jogador.items():

    if k == 'Gools/partida':
        print()
        for i,c in enumerate(jogador['Gools/partida']):
            print(f'     No {i+1}° jogo: {c} {' Gools'if c != 1 else ' Gool'}  ') 
        print()
    else:
        print(f'{k:_<30}: {v}')

print('-'*50)
print('Relatorio do jogador:')
print('-'*50)

print(f'O jogador {jogador["Nome"]} atualmente competindo pelo time do {jogador["Time"]},\njogou um total de {jogador["Quantidade de jogos"]} jogos pelo time, tendo atualmente feito {jogador["Total de gools"]} gools\ne com aproveitamento médio de {round(jogador["Média de gools/partida"])} {'gools'if c != 1 else 'gool'} por partida. ')
print('-'*50)
print()
