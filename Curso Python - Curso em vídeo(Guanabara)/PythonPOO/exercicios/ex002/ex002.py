#DECLARAÇÃO DE CLASES
class Gafanhoto:
    '''
    Uma classe que armazena os dados de nome e idade de uma pessoa, permitindo com modulos aumentar 

    - Modulos : Possui 'aniversario' que soma mais um a idade atual cadastrada 

    - Atributos : Ela recebe 2 atributos, um de nome e um de idade sintaxe: variavl = Gafanhoto(nome, idade)

    '''
    def __init__(self, n = 'Não Cadastrado', i = 0):#METODO CONSTRUTOR
        #ATRIBUTOS DE INTANCIA 
        self.nome = n
        self.idade = i

    #DECLARAÇÃO DE METODOS
    def aniversario(self):
        self.idade +=1
    
    def __str__(self):
        
         # METODO __str__ É INTERNO DA CLASE, POR PADRÃO ELE MOSTRA O INDEREÇO NA MEMORIA DA VARIAVEL, MAS SOBREESCREVENDO PODEMOS MOSTRAR UMA MENSAGEM DIRETA QUE SERA IMPRIMIDA APENAS COM O CHAMAMENTO DO OBJETO NA FUNÇÃO PRINT()

        return f'O gafanhoto {self.nome} tem {self.idade} anos'


#DECLARAÇÃO DE OBJETOS
g1 = Gafanhoto('Warlen', 21)
g1.aniversario()
print(g1.mensagem())

g2 = Gafanhoto('Kenia', 20)
print(g2.mensagem())

g3 = Gafanhoto()
print(g3.mensagem())

print(g1.__doc__)
