from rich import print
from rich.table import Table #IMPORTA A CLASSE TABELA

tabela = Table(title='Tabela de preços')

tabela.add_column('Nome')

tabela.add_column('Preço', style='red' \
'')

tabela.add_row('lapis', 'R$ 2,00')


print(tabela)