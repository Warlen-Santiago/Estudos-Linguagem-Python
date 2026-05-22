from .funcionario import Funcionario


class Horista(Funcionario):
    def __init__(self, nome, valor_hora, horas_trab):
        super().__init__(nome, sal_bruto=None)
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab

    def calc_sal(self):
       
        self.sal_bruto = self.valor_hora * self.horas_trab
        self.sal_liquido = self.sal_bruto - (self.sal_bruto * Funcionario.INSS)
    

class Mensalista(Funcionario):
    def __init__(self, nome, sal_bruto=Funcionario.SAL_MIN):
        super().__init__(nome, sal_bruto)


    def calc_sal(self):
        
        self.sal_liquido = self.sal_bruto - (self.sal_bruto * Funcionario.INSS)

    