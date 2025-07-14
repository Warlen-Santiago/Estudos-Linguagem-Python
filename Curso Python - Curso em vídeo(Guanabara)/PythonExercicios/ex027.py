nome = input('Insira seu nome completo: ')

list_nome = nome.split()

print(f'O primeiro nome é {list_nome[0]}. ')
print(f'O ultimo nome é {list_nome[len(list_nome) - 1]}. ')
