from datetime import datetime

#Pegando dado do ano atual
anoatual = datetime.now().year

print()
print('CADASTRO: ')
print('-'*50)

pessoa = {
    'Nome' : input('Nome: ').capitalize(),
    'Ano de nascimento' : int(input('Ano de nascimento: ')),
    'CTPS' : int(input('N° Carteira de trabalho[caso não tenha insira 0]: '))
}

print('-'*50)

if pessoa['CTPS'] != 0:
    situação_trabalho = ''
    while situação_trabalho not in ('N','S'):
        situação_trabalho = input('Trabalha de carteira assinada?[S/N]')[0].upper().strip()

    if situação_trabalho == 'S':
        pessoa['Dados trabalhistas'] = {
            'Ano de contratação' : int(input('Ano de contratação: ')),
            'Salário' : float(input('Salário: ')),
            'Função' : input('Função: ').capitalize()
        }
    else:
        pessoa['Dados trabalhistas'] = 'Não trabalha de carteira assinada.'

print('-'*50)
print('Dados coletados: ')
print()

for k, v in pessoa.items():

    if k != 'Dados trabalhistas':
        print(f'{k}: {v}')
    else:
        if situação_trabalho == 'S':
            for k, v in pessoa['Dados trabalhistas'].items():
                print(f'{k}: {v}')

print()           
print('-'*50)

idade = anoatual-pessoa["Ano de nascimento"]
print(f'{pessoa["Nome"]} tem {idade} anos de idade. ')

if pessoa['CTPS'] == 0:
    print('E não possui carteira de trabalho.')
elif pessoa['CTPS'] != 0 and situação_trabalho == 'N':
    print(f'{pessoa["Dados trabalhistas"]}')
else:
    idade_de_aposentadoria = idade + (35 - (anoatual - pessoa['Dados trabalhistas']['Ano de contratação']))
    print(f'Foi contratado em {pessoa['Dados trabalhistas']['Ano de contratação']} e se aposentara com {idade_de_aposentadoria} em {anoatual + (35 - (anoatual - pessoa['Dados trabalhistas']['Ano de contratação']))}')
