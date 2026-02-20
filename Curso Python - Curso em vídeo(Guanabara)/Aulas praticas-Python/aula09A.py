print('Manipulando Strings')
#Toda str que armazenamos tem um espaço na memória, mas dentro desses espaços temos macro espaços que são reservados de cada letra que são determinados pela quantidade de caracteres da palavra em qustão, mas também são reservados espaços para espacos, caracteres especiais e coisas do tipo, também destaca-se que toda string tem sua primeira casa no digito 0 e por assim diante sendo [0][1][2][3][4]

frase = 'Curso em video Python'

#mostra o que ha na decima casa, a casa nove levando em consideração que começamos do 0
print(frase[9])

#mostra o resultado da casa 0 ate a casa 9
print(frase[0:9])

#mostra o resultado da casa 0 ate a acasa 10 pulando um e mostrando o segundo como indicado pelo numero 2
print(frase[0:10:2])

#quando não indicado antes dos dois pontos o inicio ele pega automatico da casa 0 ou seja do inicio da string
print(frase[:9])

#o mesmo serve para o contrario em que ele vai mostrar ate o final da string ou seja a ultima casa de acordo com o tamanho da string
print(frase[6:])

#conta quantos caracteres há na string
print(len(frase.strip()))

#conta quantas o que foi indicado entre os parentesses aparece na string, dstaque para o fato de que se diferencia letras maiusculas e minusculas como caracteres diferentes
print(frase.count('o'))

#faz a mesma contagem que o comando anterior mas agora dentro de um espaço especifico
print(frase.count('o',0,13))

#busca o trecho especificado dentro da string, caso não seja encontrado ele retorna -1
print(frase.find('deo'))

#faz a busca da string especificada entre as aspas e retorna um valor boleano(bool) true or false
print('Curso' in frase)

#faz a subistituição do primeiro trecho especificado pelo segundo 
print(frase.replace('Python', 'Android'))

#passa de minusculo para maiusculo 
print(frase.upper())

#passa de maiusculo para minusculo
print(frase.lower())

#deixa somente a primeira letra da string maiuscula
print(frase.capitalize())

#coloca a primeira letra de cada palavra em maiusculo
print(frase.title())

#remove espaços desnecessarios no começo e no final da str por padrão, mas pode ser especificado 
print(frase.strip())
print(frase.lstrip())
print(frase.rstrip())

#faz uma divisão da str de acordo com seus espaços, por padrão de escrita divide em palavras, criando uma lista com tais, levando isso em consideração deve usar uma variavel que ira receber a lista 
lista = frase.split()
print(lista)

#da mesma forma que podemos dividir em uma lista podemos fazer a junção, o que vai ser usado para a junção é especificado entre '', pode ser um espaço vazio ou qualquer outro caractere 
print('-'.join(lista)) 
