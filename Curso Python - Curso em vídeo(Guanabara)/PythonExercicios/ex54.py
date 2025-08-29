import datetime
print('Insira os usuarios e seus anos de nascimento: ')

'''INICIALIZAÇÃO DE LISTAS'''
listname = []
listano = []

for c in range(0,7):
    nome = input('Nome: ')
    ano = int(input('Ano de nascimento: '))

    listname.append(nome)
    listano.append(ano)

ano_atual = datetime.datetime.now().year

'''INICIALIZAÇÃO DE VARIAVEL'''
soma = 0

for c in range(0, 8):
    if  ano_atual - listano[c] >= 21:
        soma = soma + 1

print(f'Com base nos dados fornecidos e considerando a maior idade acima de 21 anos dessas pessoas: \033[0;32;40m {soma} são maiores\033[0;37;m e \033[0;31;40m{c-soma} são menores\033[m. ')
