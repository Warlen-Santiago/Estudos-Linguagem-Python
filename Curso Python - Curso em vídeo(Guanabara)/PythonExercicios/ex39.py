import datetime

ano_nascimento = int(input('Insira o ano de nascimento: '))

ano_atual = datetime.datetime.now().year

idade = ano_atual - ano_nascimento

if idade == 18:
    print('Já é hora de se alistar! ')
elif idade < 18:
    print(f'Ainda não é hora de se alistar, falta {18-idade} anos para seu alistamento! ')
else:
    print(f'Já passou {idade-18} anos do seu alistamento, se enchaminhe para um quartel de alistamento para realiza-lo. ')
