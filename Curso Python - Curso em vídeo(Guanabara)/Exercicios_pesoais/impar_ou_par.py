try:

    num = int(input('Insira um número para verificar se ele é par ou impar:\n '))

    if num % 2 == 0:
        print(f'O número {num} é par!')
    else:
        print(f'O número {num} é impar!')

except ValueError:
    print('Insira um valor inteiro!')
