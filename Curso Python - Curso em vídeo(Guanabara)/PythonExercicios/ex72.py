from num2words import num2words

numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 )

escolha = -1
while escolha not in numeros:
    escolha = int(input('Escolha um número inteiro de 1 a 20: '))
    print()

    if escolha in numeros:
        extenso = num2words(numeros[escolha-1], lang='pt_BR')
        print(f'O número {numeros[escolha-1]} por extenso é {extenso}. ')
        print()
