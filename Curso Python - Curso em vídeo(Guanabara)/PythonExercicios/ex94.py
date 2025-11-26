print(f'{'CADASTRO DE PESSOAS':^50} ')
print('-'*50)

pessoas = []
while True:
    p = {
        'Nome' : input('Nome: ').capitalize(),
        'Idade' : int(input('Idade: '))
    }
    p['Sexo'] = ''
    while p['Sexo'] not in ('M','F'):
        p['Sexo'] = input('Sexo:[M/F]')[0].upper().strip()
        if p['Sexo'] not in ('M','F'):
            print('-Por favor insira um valor entre M ou F ')

    pessoas.append(p)
    escolha = ''
    while escolha not in ('N', 'S'):
        escolha = input('Deseja cntinuar:[S/N] ')[0].upper().strip()
    print()
    if escolha == 'N':
        break

print('-'*50)
print(f'{'DADOS CADASTRADOS':^50} ')
print('-'*50)

print(f'Foram cadastradas {len(pessoas)} pessoas. ')
print()

s_idade = 0

for c in pessoas:
    for k,v in c.items():
        if k == 'Idade':
            s_idade+=v

med_idade = s_idade/len(pessoas)

print(f'A média de idade do grupo é {med_idade:.2f}. ')
print('-'*50)

print('As mulheres cadastradas foram:')
for c in pessoas:
    for k,v in c.items():
        if k == 'Sexo' and v == 'F':
            print(f'-{c['Nome']}')
print()

print('As pessoas com idade acima da média são: ')
for c in pessoas:
    for k,v in c.items():
        if k == 'Idade' and v > med_idade:
            print(f'-{c['Nome']} com {c['Idade']} anos.')

print()
print('-'*50)
print()
           