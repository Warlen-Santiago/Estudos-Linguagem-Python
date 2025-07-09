nome = input('Insira seu nome: ')

v = nome.find('Silva')
v2 = nome.find('silva')

if 'silva' in nome or 'Silva' in nome:
    print('Seu nome contem silva')
else:
    print('Seu nome não contem silva')