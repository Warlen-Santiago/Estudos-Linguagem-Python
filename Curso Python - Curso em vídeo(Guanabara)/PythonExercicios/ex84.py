pessoas = []
dados = []
maisp = []
menosp = []

print('Insira os dados:')
print()

while True:
    dados.append(input('Nome: ').capitalize())
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:]) 
    dados.clear()

    escolha = ''
    while escolha not in ('N', 'S'):
        escolha = (input('Deseja continuar: [S/N] '))[0].upper().strip()
    if escolha == 'N':
        break

print('-'*40)
print(f'Foram cadastradas {len(pessoas)} pessoas. ')
print()

for p in pessoas:
    if p[1] >= 85:
        maisp.append(p[0])

if maisp:
    if len(maisp) > 1:
        print(f'As pessoas mais pesadas da lista (85kg para mais) são {maisp}')
    else:
        print(f'A pessoa mais pesada da lista (85kg para mais) é {maisp[0]}')
else:
    print('Na lista não há pessoas com mais de 85Kg. ')
print()

for p in pessoas:
    if p[1] < 65:
        menosp.append(p[0])
if menosp:
    if len(menosp) > 1:
        print(f'As pessoas mais leves da lista (65kg para menos) são {menosp}')
    else:
        print(f'A pessoa mais leve da lista (65kg para menos) é {menosp[0]}')
else: 
    print('Na lista não há pessoas com menos de 65Kg. ')
print()
