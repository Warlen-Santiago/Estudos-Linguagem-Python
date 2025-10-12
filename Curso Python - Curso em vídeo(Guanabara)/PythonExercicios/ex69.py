print('-'*20)
print('Cadastro de pessoas')
print('-'*20)

maisd18 = 0
homens = 0
mulhermenosd20 = 0

while True:
    sexo = ''
    while sexo not in  ['M', 'F']:
        sexo = input('Sexo [M/F]: ')[0].strip().upper()
    idade = 0
    while idade <= 0 or idade > 120:
        idade = int(input('Idade: '))

    if idade > 18:
        maisd18+=1
    if sexo == 'M':
        homens+=1
    if sexo == 'F' and idade < 20:
        mulhermenosd20+=1
    
    escolha = ''
    while escolha not in  ['S', 'N']:
        escolha = input('Quer continuar [S/N]: ')[0].strip().upper()

    if escolha == 'N':
        break

print('-'*20)

print(f'Foram cadastradas {maisd18} pessoas com mais de 18 anos. ')
print()
print(f'Foram cadastrados {homens} homens. ')
print()
print(f'Foram cadastradas {mulhermenosd20} mulheres com menos de 20 anos. ')

