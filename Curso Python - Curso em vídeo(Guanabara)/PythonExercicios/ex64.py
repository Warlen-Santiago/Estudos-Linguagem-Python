n=0
list_n=[]
contador=1

print('Insira números inteiros(o programa para quando for inserido 999 que não é incluido): ')
print()

while n != 999:
    n = int(input(f'{contador}°: '))

    if n != 999:
        list_n.append(n)
    contador+=1

print()
print(f'Foram digitados {len(list_n)} números, e a soma entre eles é {sum(list_n)}. ')
