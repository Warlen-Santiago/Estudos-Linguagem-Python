from abc import ABC, abstractmethod


class Poligono(ABC):
    def __init__(self, quant_lados):
        self.quant_lados = quant_lados


    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass
        