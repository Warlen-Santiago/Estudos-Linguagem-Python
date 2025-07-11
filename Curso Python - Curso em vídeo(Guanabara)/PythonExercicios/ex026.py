frase = input('Insira uma frase qualquer: ')

quant_a = frase.count('a')
quant_A = frase.count('A')

quant_Aa = quant_a + quant_A

print(f'Nessa frase a letra A apareceu um total de: {quant_Aa} vezes. ')

inicio_a = frase.find('a')
inicio_A = frase.find('A')

if inicio_A == -1:
    print(f'A letra A aparece pela primeira vez na casa {inicio_a} isso contando os espaços. ')
else:
     print(f'A letra A aparece pela primeira vez minuscula na casa {inicio_a} e maiuscula na casa {inicio_A}, isso contando os espaços. ')
