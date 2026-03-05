from rich import print
from rich.panel import Panel
from time import sleep


class Livro():
    def __init__(self, nome, paginas, pg_atual=1):
        self.nome = nome
        self.pgs = paginas
        self.pg_atual = pg_atual

        apresentação = Panel(f'📚 📖[blue] Você acabou de abrir o livro[/] [red]"{self.nome}"[/],[blue] que tem [/][green]{self.pgs} paginas[/] ,[blue] agora você está na pagina:[/][green] 1[/]')
        print(apresentação)

    def avançar_pg(self, quant_pg):

        for pg in range(1,quant_pg+1):
            if self.pg_atual == self.pgs:
                print(f'[blue]Parabens!🥳🥳, Você chegou ao final da sua leitura, terminou o livro[/][red] "{self.nome}"[/]')
                break

            else:
                print(f'Pg: {self.pg_atual}', end='--> ')
                self.pg_atual +=1
                sleep(0.4)

                if pg == quant_pg:
                    print(f'[blue]Você avançou [/][green]{quant_pg} paginas[/],[blue] e está agora na pagina:[/][green] {self.pg_atual}[/]')


livro1 = Livro('O Mundo de sofia', 14)

livro1.avançar_pg(3)
livro1.avançar_pg(6)
livro1.avançar_pg(4)
livro1.avançar_pg(3)
