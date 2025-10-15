print('-'*80)
print('TABUADA' )
print('-'*80)

while True:
    n = int(input('Insira um número qualquer para ver sua tabuada[número negativo para parar]:' ))
    print('-'*80)
    if n < 0:
        break
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
    print('-'*80)
print('Programa encerrado.')
