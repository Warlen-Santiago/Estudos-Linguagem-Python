from .base_cardapio import BebidaQuente


class Cafe(BebidaQuente):
    def __init__(self):
        super().__init__()
    

    def misturar(self):
        return f'Passando agua fervente pelo pó de café.'
    

    def servir(self):
        return f'Servindo puro em xícara P - Acompanha sache de açucar.'
    


class Leite(BebidaQuente):
    def __init__(self):
        super().__init__()

    
    def misturar(self):
        return f'Passando vapor pressurizado pelo bico do leite.'
    

    def servir(self):
        return f'Servido em caneca G - Acompanha cafe, canela e cacau em pó.'
    

class Cha(BebidaQuente):
    def __init__(self):
        super().__init__()


    def misturar(self):
        return f'Deixando sache de ervas de molho por 5 minutos'
    

    def servir(self):
        return f'Servido em xícara M - Acompanha mel e gengibre.'