from random import randint

n1 = randint(0,10)
n2 = randint(0,10)
n3 = randint(0,10)
n4 = randint(0,10)
n5 = randint(0,10)

tupla = (n1, n2, n3, n4, n5)

print(tupla)

print(f'O maior n´mero sorteado foi {max(tupla)} e o menor foi {min(tupla)}. ')
