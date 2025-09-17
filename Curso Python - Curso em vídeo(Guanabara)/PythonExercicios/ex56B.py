'''inicialisando as variaveis'''
soma_idade = 0
media_idade = 0
maior_idade_homen = 0
nome_h_maior_idade = ''
total_mulheres_m20 = 0

'''Estrutura de entrada dos dados'''
for p in range (1,5):
    print(f'----- {p}° PESSOA -----')
    nome = input('nome: ').strip()
    sexo = input('sexo[M/F]: ').upper().strip()
    idade = int(input('idade: '))

    '''somando idade total do grupo'''
    soma_idade += idade

    '''Buscando homen mais velho'''
    if p == 1 and sexo == 'M':
        maior_idade_homen = idade
        nome_h_maior_idade = nome
    elif sexo == 'M' and maior_idade_homen < idade:
            maior_idade_homen = idade
            nome_h_maior_idade = nome 

    '''Descobrindo quantas mulheres tem menos de 20 anos'''
    if sexo == 'F' and idade < 20:
         total_mulheres_m20 += 1

'''calculando media idade do grupo'''
media_idade = soma_idade/4

print(f'A média de idade do grupo é de {media_idade} anos. ')

if maior_idade_homen == 0:
     print('Não há homen mais velho, pois não há homens no grupo. ')
else:
     print(f'O homen mais velho é {nome_h_maior_idade.capitalize()} e ele tem {maior_idade_homen} anos. ')

print(f'No grupo há {total_mulheres_m20} mulheres com menos de 20 anos. ')