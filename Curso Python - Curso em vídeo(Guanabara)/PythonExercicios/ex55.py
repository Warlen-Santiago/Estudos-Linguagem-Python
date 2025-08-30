pesos = []
nomes = []
print('Insira um nome e peso correspondente para cada pessoa:' )
for c in range(0, 5):
    nome = input('nome:' )
    peso = float(input('peso:' ))
    pesos.append(peso)
    nomes.append(nome)

maior_peso = max(pesos)
nome_maior_peso = pesos.index(maior_peso)

menor_peso = min(pesos)
nome_menor_peso = pesos.index(menor_peso)

print(f'O maior peso é de {nomes[nome_maior_peso]} e seu peso é {maior_peso}Kg.' )
print(f'O menor peso é de {nomes[nome_menor_peso]} e seu peso é {menor_peso}Kg.' )

