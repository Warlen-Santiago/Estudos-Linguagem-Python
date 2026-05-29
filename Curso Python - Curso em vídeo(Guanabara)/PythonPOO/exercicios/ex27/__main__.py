from rich import print, inspect
import lib as l
import random as r
from time import sleep

def main():
    list_golpes_mago = [{
        'nome_atk' : 'Bola de fogo',
        'dano_atk' : 20
    },{
        'nome_atk' : 'Raios',
        'dano_atk' : 20
    },{
        'nome_atk' : 'Shadow ball',
        'dano_atk' : 60
    }]

    list_golpes_guerreiro = [{
        'nome_atk' : 'Avanço ',
        'dano_atk' : 20
    },{
        'nome_atk' : 'Corte pesado',
        'dano_atk' : 60
    },{
        'nome_atk' : 'lamina sangrenta',
        'dano_atk' : 70
    }]

    list_golpes_paladino = [{
        'nome_atk' : 'Avanço com escudo',
        'dano_atk' : 20
    },{
        'nome_atk' : 'Ataque pesado',
        'dano_atk' : 40
    },{
        'nome_atk' : 'Ruptura divina',
        'dano_atk' : 60
    }]

    player1 = l.Mago('alduim', 'humano',list_golpes_mago )
    player2 = l.Guerreiro('Kratos', 'Semi-Deus', list_golpes_guerreiro)
    player3 = l.Paladino('Pike', 'Anão', list_golpes_paladino)

    participantes = [player1, player2, player3]
    

    round = 1
    while True:
        print(f'{'-'*10} {round}° RODADA {'-'*10}')

        sleep(1)

        jogador = r.choice(participantes)
        movimento = r.randint(1,4)

        if movimento >=2:
            alvo = r.choice(participantes)
            while alvo == jogador:
                alvo = r.choice(participantes)

            jogador.atacar(alvo)
            sleep(1)

        else:
            jogador.curar()
            sleep(1)

        if player1.vida <= 0 or player2.vida <= 0 or player3.vida <= 0:
            print(f'{'-'*10} FIM DE JOGO - {round}° RODADA {'-'*10}')
            break
        round +=1



if __name__ == '__main__':
    main()