n = int(input('Digite um Número: '))
t = 0
for c in range(1,n+1):
    if n % c == 0:
        print('\033[32m', end=' ')
        t+=1
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')
print('\n')
print(f'\033[mO número {n} foi divisível {t} vezes. ')
if t == 2:
    print('É PRIMO! ')
else:
    print('NÃO É PRIMO ')
