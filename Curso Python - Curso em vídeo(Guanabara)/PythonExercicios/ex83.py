print('Testando expressões aritméticas com parenteses... ')
print('-'*40)

print('insira uma expressão e vamos ver se ela é valida com base em seus parenteses... ')
ex = input('insira sua expressão: ')
lista_ex = list(ex)

pa = lista_ex.count('(')
pf = lista_ex.count(')')

print(f' {pa} e {pf}')

print('-'*40)

if pa == pf:
    print('Sua expressão é valida! ')
else:
    print('Sua expressão é invalida. :(')