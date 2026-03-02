from time import sleep
class ContaBancaria:
    '''

    Cria uma conta bancaria que permite fazer depositos e saques

    '''
    def __init__(self, id, nome, saldo = 0.0):

        # DEFINIÇÃO DOS ATRIBUTOS
        
        self.id = id 
        self.titular = nome
        self.saldo = saldo

    def __str__(self):
        return f'- Titular da conta : {self.titular} \n- id : {self.id} \n- saldo : R$ {self.saldo:.2f}\n '
    
    def depositar(self, valor=0.0):
        self.saldo +=valor
        print(f'Deposito de R${valor:.2f} realizado com sucesso!\n ')

    def sacar(self, valor=0.0):
        if self.saldo<valor:
            print(f'Saque de R${valor:.2f} NEGADO - Saldo insuficiente\n ')
        else:
            self.saldo -= valor
            print(f'Saque de R${valor:.2f} realizado com sucesso!\n ')

'''_____________________________________________________________________________________________________________________________________________'''


conta1 = ContaBancaria(3252, 'Warlen Santiago Paixão Oliveira', 2053.17)

print(conta1)
sleep(3)
conta1.depositar(123.57)
sleep(1)
conta1.sacar(3000)
sleep(1)
print(conta1)
