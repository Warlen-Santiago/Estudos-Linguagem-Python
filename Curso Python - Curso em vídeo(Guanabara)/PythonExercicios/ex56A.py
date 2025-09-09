pessoas = []

print('Insira Nome, Idade e Sexo( M ou F ) correspondente para cada indivíduo: ')

for c in range(4):
    pessoa = {
        'nome' : input('Nome: '),
        'idade' : int(input('Idade: ')),
        'sexo' : input('Sexo: ').upper()
    }
    pessoas.append(pessoa)

idades = [p['idade']for p in pessoas]
media = sum(idades) / len(idades)

print(f'Entre os indivíduos listados a média de idade é de {media:.1f} anos. ')

homens = [p for p in pessoas if p['sexo'] == 'M']
if homens:
    homem_mais_velho = max(homens, key=lambda x: x['idade'])
    print(f'O homem mais velho é {homem_mais_velho["nome"]} com {homem_mais_velho["idade"]} anos.')
else:
    print('Não há homens no grupo.')

mulheres_jovens = [p for p in pessoas if p['sexo'] == 'F' and p['idade'] < 20]
print(f'Nesse grupo há {len(mulheres_jovens)} mulher(es) com menos de 20 anos.')
