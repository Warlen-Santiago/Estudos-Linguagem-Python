try:
    num = int(input('Insira um número: '))

    if num % 2 == 0:
        print(f'O número {num} é par ')
    else:
        print(f'O número {num} é impar ')
except ValueError:
    print('O valor inserido não é valido, Certifique-se de inserir um número inteiro ')
