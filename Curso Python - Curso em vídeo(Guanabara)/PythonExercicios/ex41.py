import datetime

print('Categorias de atletas de natação por idade:')
ano_nascimento = int(input('Insira o ano de nascimento do atleta: '))

ano_atual = datetime.datetime.now().year

idade = ano_atual - ano_nascimento

if idade <= 9:
    print('Atleta Mirim.')
elif idade <= 14:
    print('Atleta Infantil.')
elif idade <= 19:
    print('Atleta Junior.')
elif idade <= 20:
    print('Atleta Senior.')
else:
    print('Atleta Master.')

