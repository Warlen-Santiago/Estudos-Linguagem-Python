from rich import print
from rich.panel import Panel


class Funcionario:
    #ATRIBUTO DE CLASSE
    empresa = 'Escritorio araujo e mendes'
    # DEFININDO ATRIBUTOS DE INSTANCIA DO OBJETO
    def __init__(self, nome='Não informado', setor='Não informado', cargo='Não informado'):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    # DEFININDO METODOS
    def apresentação(self):
        painel = Panel((f'Olá, Muito prazer!😁 Me chamo [purple]{self.nome}[/], sou [purple]{self.cargo}[/] e atuo no stor de [purple]{self.setor} na empresa {Funcionario.empresa}[/]'))

        return painel


funcionario01 = Funcionario('Warlen', 'Organização e atendimento', 'Assistente Jurídico')
print(funcionario01.apresentação())

