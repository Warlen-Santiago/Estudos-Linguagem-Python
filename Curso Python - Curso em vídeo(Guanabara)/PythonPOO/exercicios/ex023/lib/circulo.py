from .poligono import Poligono
from rich.panel import Panel


class Circulo(Poligono):
    def __init__(self, raio):
        super().__init__(quant_lados = 1)
        self.raio = raio

    def area(self):
        area = 3.14 * (self.raio * self.raio)

        return area
    

    def perimetro(self):
        perimetro = 3.14 * (self.raio * 2)
        
        return perimetro
    
    def exibir(self):
        exibir = Panel(f'Para um circulo de raio: {self.raio}\nsua área: {self.area():.2f}\nseu perimetro: {self.perimetro():.2f}', expand=False)
        return exibir