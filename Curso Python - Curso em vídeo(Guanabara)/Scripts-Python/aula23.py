try:
    a = int(input('Primeiro valor: '))
    b = int(input('Segundo valor: '))
    r = a / b
except (ValueError, TypeError):
    print(f'O tipo de dado inserido foi invalido... ')
except ZeroDivisionError:
    print('Divisão de base 0 é invalida... ')
except KeyboardInterrupt:
    print('O usuario ecerrou o programa... ')
else:
    print(f'O resultado é: {r:.1f} ')
finally:
    print('Programa encerrado... Volte sempre!')