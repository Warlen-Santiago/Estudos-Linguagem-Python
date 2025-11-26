from math import ceil

print()
print(f'{'QUALIFICAÇÃO DOS JOGADORES':^50} ')
print('-'*50)

print('insira os dados correspondentes: ')
print()

jogares = []
while True:
    jogador = {
        'Nome' : input('Nome do jogador: ').capitalize(),
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

    jogares.append(jogador)

    escolha = ''
    while escolha not in ('N','S'):
        escolha = input('Quer continuar?[S/N] ')[0].upper().strip()
    print('-'*50)

    if escolha == 'N':
        break
#-----------------------------CORRIGIR FORMATAÇÃO-----------------------------------------------------
print(f'{'ID Nome':<10}{'Gols':^20}{"Total Goals":>20}')
print('-'*50)

for i,c in enumerate(jogares):
    print(f'{i}.{c['Nome']:<10}{str(c['Gools/partida']):^19}{str(c['Total de gools']):>18}')
#-----------------------------------------------------------------------------------------------------

print('-'*50)
while escolha != 999:

    escolha = int(input('Você deseja ver dados de qual jogador?[insira o ID/999 para parar] '))

    if escolha >= 0 and escolha <= len(jogares)-1:

        print(f'-- LEVANTAMENTO DO JOGADOR {jogares[escolha]['Nome']}')
        print()
        for i,c in enumerate(jogares[escolha]['Gools/partida']):
            print(f'• No {i+1}° jogo fez {c} {'Gols' if c !=1 else 'Gol'}')
        print()
        
    elif escolha == 999:
        break
    else:
        print('Opção inválida, tente novamente.[999 para parar] ')
    print('-'*50)
    
print('PROGRAMA ENCERADO.')
print('-'*50)
print()
