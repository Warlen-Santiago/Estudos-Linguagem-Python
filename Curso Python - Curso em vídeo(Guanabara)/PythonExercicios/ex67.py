print('-'*80)
print('TABUADA' )
print('-'*80)

while True:
    n = int(input('Insira um número qualquer para ver sua tabuada[número negativo para parar]:' ))
    print('-'*80)
    if n < 0:
        break
    print(f'''
            {n} x 1 = {n*1}
            {n} x 2 = {n*2}
            {n} x 3 = {n*3}
            {n} x 4 = {n*4}
            {n} x 5 = {n*5}
            {n} x 6 = {n*6}
            {n} x 7 = {n*7}
            {n} x 8 = {n*8}
            {n} x 9 = {n*9}
            {n} x 10 = {n*10}
''')
    print('-'*80)
print('Programa encerrado.')