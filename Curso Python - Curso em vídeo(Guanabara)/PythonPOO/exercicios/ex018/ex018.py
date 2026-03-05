from rich import print
from rich.panel import Panel


class Churas():
    def __init__(self, titulo='Churasco', pessoas=1):
        self.quant = pessoas
        self.titulo = titulo

    def analise(self, valorKg=35.70, quant_consum=0.600):

        quant_carne = self.quant * quant_consum
        total_custo = quant_carne * valorKg
        valor_pessoa = total_custo/self.quant

        resultado = Panel(f'O churasco para {self.quant} pessoas tem estimativa de {quant_carne:.3f} Kg de carne no total\n o custo total do churasco saira em R$ {total_custo:.2f} e o individual R$ {valor_pessoa:.2f}', title=self.titulo, expand=False)

        return resultado
    

churasco1 = Churas(pessoas=20)
print(churasco1.analise())
