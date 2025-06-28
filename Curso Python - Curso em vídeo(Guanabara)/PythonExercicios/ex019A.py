from random import choice

a1 = input('Insira o nome do primeiro aluno:\n ')
a2 = input('Insira o nome do segundo aluno:\n ')
a3 = input('Insira o nome do terceiro aluno:\n ')
a4 = input('Insira o nome do quarto aluno:\n ')

lista = [a1, a2, a3, a4]
aluno_escolhido = choice(lista)

print(f'O aluno escolhido foi {aluno_escolhido}! ')