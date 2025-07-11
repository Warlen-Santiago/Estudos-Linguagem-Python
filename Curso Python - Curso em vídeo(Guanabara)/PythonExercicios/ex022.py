nome = input('Insira seu nome completo:\n ').strip

print('Com todas as letras maiusculas:\n ')
print(nome.upper())

print('Com todas as letras minusculas:\n ')
print(nome.lower())

nomes = nome.split()
print('Quantidade de letras do primeiro nome:\n ')
print(len(nomes[0]))

nomes_semspc = ''.join(nomes)
print('Quantidade de letras do nome:\n ')
print(len(nomes_semspc))