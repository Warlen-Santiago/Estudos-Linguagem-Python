from ..classes import Caminhão, Moto, Drone
from rich.table import Table


def tabela_fretes(distancia):
    
    tabela = Table(title=f'Fretes para distancia de {distancia} km')

    t1 = Caminhão(distancia)
    t2 = Moto(distancia)
    t3 = Drone(distancia)


    tabela.add_column('Distancia')
    tabela.add_column('Veículo')
    tabela.add_column('Valor')

    tabela.add_row(f'{distancia}Km', f'{type(t1).__name__}', f'{t1.calc_frete()}')
    tabela.add_row(f'{distancia}Km', f'{type(t2).__name__}', f'{t2.calc_frete()}')
    tabela.add_row(f'{distancia}Km', f'{type(t3).__name__}', f'{t3.calc_frete()}')


    return tabela


