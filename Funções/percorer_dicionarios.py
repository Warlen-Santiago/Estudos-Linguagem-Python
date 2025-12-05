def listar(dicionario):
    for k, v in dicionario.items():
        print(f'{k}: {v}')

def linha():
    print('-'*50)

linha()
print('Insira os dados conforme pedido: ')
linha()

pessoas = []
for c in range(0, 3):
    pessoa = {
        'Nome':input('Nome:' ).capitalize(),
        'Idade':int(input('Idade: ')),
        'Profissão':input('Profissão:').capitalize()
    }
    pessoas.append(pessoa)
    print()

linha()
print('Pessoas cadastradas:')
linha()

for c in pessoas:
    listar(c)
    print()
