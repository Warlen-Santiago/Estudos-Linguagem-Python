print('-'*40)
print('LISTA DE COMPRAS' )
print('-'*40)

total = mais_d1000 = 0
mais_barato = ''
valor_mais_barato = 0
produtos_mais_baratos = []

while True:
    produto = input('Produto: ')
    valor = float(input('Valor: R$'))

    total+=valor

    if valor > 1000:
        mais_d1000+=1

    if mais_barato == '':
        mais_barato = produto
        valor_mais_barato = valor

    elif valor < valor_mais_barato:
        mais_barato = produto
        produtos_mais_baratos.append(mais_barato)
        valor_mais_barato = valor

    elif valor == valor_mais_barato:
        produtos_mais_baratos.append(produto)

    escolha = ''
    while escolha not in ['S', 'N']:
        escolha = input('Quer continuar [S/N]: ')[0].strip().upper()
    if escolha == 'N':
        break

print('-'*40)

print(f'O total gasto foi R${total:.2f}. ')
print()
print(f'{mais_d1000} produto(s) custa(m) mais de mil reais. ')
print()

if len(produtos_mais_baratos) < 2:
    print(f'O produto mais barato foi "{mais_barato}" e custou R${valor_mais_barato:.2f}. ')
else:
    print(f'Os produtos mais baratos foram {produtos_mais_baratos} e eles custaram R${valor_mais_barato:.2f} cada. ')