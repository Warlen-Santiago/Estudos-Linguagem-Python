from .transporte import Transporte


class Moto(Transporte):
    fator = 0.50

    def __init__(self, distancia):
        super().__init__(distancia)

    
    def calc_frete(self):

        self.frete = Moto.fator * self.distancia

        return f'R$ {self.frete}'
    

class Drone(Transporte):
    fator = 9.50

    def __init__(self, distancia):
        super().__init__(distancia)


    def calc_frete(self):
        if self.distancia > 10:
            return f'Distancia maxima de 10Km para entregas'

        else:
            self.frete = Drone.fator * self.distancia

        return f'R$ {self.frete}'
    

class Caminhão(Transporte):
    fator = 1.20

    def __init__(self, distancia):
        super().__init__(distancia)


    def calc_frete(self):
        if self.distancia < 50:
            return f'Distancia minima 50km para entregas'
        
        else:
            self.frete = Caminhão.fator * self.distancia

        return f'R$ {self.frete}'