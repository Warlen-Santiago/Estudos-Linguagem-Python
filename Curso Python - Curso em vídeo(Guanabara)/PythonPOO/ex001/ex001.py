#DECLARAÇÃO DE CLASES
class Gafanhoto:
    def __init__(self):#METODO CONSTRUTOR
        #ATRIBUTOS DE INTANCIA 
        self.nome = ''
        self.idade = 0

    #DECLARAÇÃO DE METODOS
    def aniversario(self):
        self.idade +=1

    def mensagem(self):
        return f'O gafanhoto {self.nome} tem {self.idade} anos'


#DECLARAÇÃO DE OBJETOS
g1 = Gafanhoto()
g1.nome = 'Warlen'
g1.idade = 21
g1.aniversario()
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = 'Kenia'
g2.idade = 20
print(g2.mensagem())