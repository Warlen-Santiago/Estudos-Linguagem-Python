print('Insira números inteiros(o programa para quando for inserido 999): ')
print()

n = contador = soma = 0

while n != 999:

    n = int(input(f'{contador+1}°: '))

    if n != 999:
        contador+=1
        soma += n

print()
print(f'Foram digitados {contador} números, e a soma entre eles é {soma}. ')
