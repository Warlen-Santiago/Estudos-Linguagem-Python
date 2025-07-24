print('Convertendo números inteiros para Binário - Octal - Hexadecimal. ')
num = int(input('Insira um numero inteiro qualquer: '))
e = int(input('Agora escolha qual base para a conversão: \n1-binário \n2-Octal \n3-Hexadecimal \n '))

if e == 1:
    print(f'{num} em binário é {bin(num)[2:]} ')
elif e == 2:
    print(f'{num} em octal é {oct(num)[2:]} ')
elif e == 3:
    print(f'{num} em hexadecimal é {hex(num)[2:]} ')
else:
    print('Escolha um valor valido ')
