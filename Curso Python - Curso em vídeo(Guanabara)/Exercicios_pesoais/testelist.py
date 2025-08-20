lista = [1, 5, 2, 6, 9, 20, 'pedro']

pos = int(input('Insira a posição que o item em questão sera adicionado: '))
item = input('Insira o item: ')

lista.insert(pos-1, item)

print(lista)