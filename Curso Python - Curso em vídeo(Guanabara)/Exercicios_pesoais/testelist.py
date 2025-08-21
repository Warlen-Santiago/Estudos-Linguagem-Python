lista = [1, 5, 2, 6, 9, 20, 'pedro']

pos = int(input('Insira a posição que o item em questão sera adicionado: '))
item = input('Insira o item: ')

lista.insert(pos-1, item)

print(lista)

'''Estudando listas = [], tuplas = () e dicionarios = {}'''
print('-='*5,'Estudando listas = [], tuplas = () e dicionarios = {}','-='*5 )

print(' ')

print('As listas em python são uma otima maneira de armazenar grupos de dados. ')
print('Dentro das listas podemos armazenar qualquer tipo de dado convencional ou mesclar tipos de dados, exemplo uma lista númerica: ')

print(' ')
'''Aqui nos criamos uma lista e ja a iniciamos com itens dentro da propria, para iniciar uma lista usamos variavel = [], assim teriamos uma lista vazia, essa em questão como ja dito inicializamos com números'''
numeros = [1, 2, 3, 4, 5] 
print(numeros)
print(' ')

e1 = input('Essa é uma lista númerica, mas se quiser pode adicionar um string em seu meio, digite seu nome para adicionar a lista: ')
print(' ')

numeros.insert(3, e1)
print(numeros)