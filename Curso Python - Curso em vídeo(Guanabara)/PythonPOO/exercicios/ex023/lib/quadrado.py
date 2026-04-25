from .poligono import Poligono
from rich.panel import Panel


class Quadrado(Poligono):
    def __init__(self, tam_lado):
        super().__init__(quant_lados = 4)
        self.tam_lado = tam_lado

    def perimetro(self):
        perimetro = self.tam_lado * self.quant_lados

        return perimetro
    
    def area(self):
        area = self.tam_lado * self.tam_lado

        return area

    def exibir(self):
        exibir = Panel( f'Para um quadrado de lado: {self.tam_lado}\nsua área: {self.area():.2f}\nseu perimetro: {self.perimetro():.2f} ', expand=False)
        
        return exibir