print(' '*5,'Gerador de sequência de Fibonacci' )
print()

n = int(input('Escolha quantas posições você deseja mostrar: '))
print()

if n == 1:
        print(f'O primeiro número da sequência de Fibonacci é 0. ')
elif n == 2:
        print(f'Os {n} primeiros números da sequência de Fibonacci são 0, 1. ')
else:
    cont = 0
    a = 0
    b = 1

    print(f'Os {n} primeiros números da sequência de Fibonacci são: ')
    print()

    while cont < n:
        if cont == 0:
              print(a, end='⭢ ')
        elif cont == 1:
              print(b, end='⭢ ')
        else:
            print(a + b, end='⭢ ')
            a, b = b, a+b
        cont+=1
print('FIM. ')
