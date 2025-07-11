nome = input('Insira seu nome completo: ')

list_nome = nome.split()

quant_list = len(list_nome)

print(f'O primeiro nome é {list_nome[0]}. ')
print(f'O ultimo nome é {list_nome[quant_list - 1]}. ')
