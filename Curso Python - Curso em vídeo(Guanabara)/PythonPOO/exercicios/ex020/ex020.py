from rich import print
from rich.panel import Panel


class Gamer():
    def __init__(self,nome,nick):
        self.nome = nome
        self.nick =nick
        self.jogos_fav = []

    def add_favorito(self,nome_jogo):
        self.jogos_fav.append(nome_jogo)
        self.jogos_fav.sort()

    def ficha(self):
        lista_jogos = '\n🎮 '.join(self.jogos_fav)
        ficha = Panel(f'[black]Nome real:[/] [red]{self.nome}[/]\n[yellow]Jogos favoritos:[/][black] \n🎮 {lista_jogos}[/] ', title=f'Player -{self.nick}-', expand=False, style='blue')
        return ficha


player1 = Gamer('warlen Santiago', 'S4NTS2')

player1.add_favorito('Terraria')
player1.add_favorito('Skyrim')
player1.add_favorito('Minecraft')
player1.add_favorito('Pop Batle')
player1.add_favorito('DBZ Budokai 3')

print(player1.ficha())
