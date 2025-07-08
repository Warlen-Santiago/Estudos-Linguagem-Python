cidade = input('Insira o nome da sua cidade para ver se ela começa com santo no nome: ')

nome_separado = cidade.split()

if nome_separado[0] == 'Santo':
    print('Sim, sua cidade começa com santo no nome! ')
elif nome_separado[0] == 'santo':
    print('Sim, sua cidade começa com santo no nome! ')
else:
    print('não, sua cidade não começa com santo no nome. ')