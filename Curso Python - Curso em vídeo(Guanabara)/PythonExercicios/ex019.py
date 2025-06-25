import random

a1 = input('Insira o nome do primeiro aluno:\n ')
a2 = input('Insira o nome do segundo aluno:\n ')
a3 = input('Insira o nome do terceiro aluno:\n ')
a4 = input('Insira o nome do quarto aluno:\n ')

num = random.randint(1,4)

if num == 1:
    print(f'O aluno escolhido foi {a1} ')
elif num == 2:
    print(f'O aluno escolhido foi {a2} ')
elif num == 3:
    print(f'O aluno escolhido foi {a3} ')
else:
    print(f'O aluno escolhido foi {a4} ')
    