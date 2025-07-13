cidade = input('Insira o nome da sua cidade para ver se ela começa com santo no nome: ').strip()

nome_separado = cidade.split()

if nome_separado[0].upper() == 'SANTO':
    print('Sim, sua cidade começa com santo no nome! ')
else:
    print('não, sua cidade não começa com santo no nome. ')