print('tabuada de multiplicação e divisão! ')
n = int(input('Escolha um número: '))

for c in range(0, 11):
    print(f'{n} X {c} = {n*c}')

print('-='*20)

for c in range(0, 11):
    print(f'{n*c} / {n} = {c}')
