from rich import print
from rich.panel import Panel


class Funcionario:

    # DEFININDO ATRIBUTOS
    def __init__(self, nome='Não informado', setor='Não informado', cargo='Não informado'):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    # DEFININDO METODOS
    def apresentação(self, empresa='Escritório Araujo e Mendes'):
        painel = Panel((f'Olá, Muito prazer!😁 Me chamo [purple]{self.nome}[/], sou [purple]{self.cargo}[/] e atuo no stor de [purple]{self.setor} na empresa {empresa}[/]'))

        return painel


funcionario01 = Funcionario('Warlen', 'Organização e atendimento', 'Assistente Jurídico')
print(funcionario01.apresentação())

