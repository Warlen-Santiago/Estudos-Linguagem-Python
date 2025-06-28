from random import shuffle

print('Sorteadno a ordem de apresentação. ')

g1 = str(input('Insira o primeiro grupo: '))
g2 = str(input('Insira o segundo grupo: '))
g3 = str(input('Insira o terceiro grupo: '))
g4 = str(input('Insira o quarto grupo: '))

lista_de_grupos = [g1, g2, g3, g4]

shuffle(lista_de_grupos)

print('A ordem embaralhada é a seguinte: ')
print(lista_de_grupos)
