compras =('nintendo switch', 1499.99, 'mouse pad', 37.00, 'calça de couro da balanceaga', 3999.00, 'papel', 2.50, 'pão', 10.00, 'bolo de milho', 15.00, 'picole', 2.50, 'mouse de morango', 6.00)

print(f'{'Lista de compras':^37}')

print('-'*37)

for c in range(0,len(compras)):
    if c % 2 == 0:
        print(f'{compras[c].capitalize():<30}',end='')
    else:
        print(compras[c])
print('-'*37)
