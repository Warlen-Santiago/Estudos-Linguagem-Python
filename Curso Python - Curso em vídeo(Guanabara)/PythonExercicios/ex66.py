cont = soma = 0
while True:
    n = int(input('Insira um número inteiro [999 para parar]:' ))
    if n == 999:
        break
    soma +=n
    cont +=1
print()
print(f'Foram inseridos {cont} números e a soma entre eles é {soma}. ')
print()
