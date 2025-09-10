n = int(input('Digite um numero inteiro qualquer para descobir se ele é primo: '))
v = 0
for c in range(1, n+1):
    if n % c == 0:
        v+=1
if v == 2:
    print(f'O número {n} é `PRIMO. ')
else:
    print(f'O número {n} não  é PRIMO. ')