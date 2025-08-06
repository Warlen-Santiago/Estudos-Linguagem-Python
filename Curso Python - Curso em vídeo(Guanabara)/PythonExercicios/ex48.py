print('Soma dos números ímpares múltiplos 3 ')

soma = 0

for c in range(0, 501, 3):
    if c % 2 > 0:
        soma = soma + c
print(soma)
