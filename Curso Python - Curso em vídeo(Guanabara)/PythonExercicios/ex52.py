n = int(input('Digite um numero inteiro qualquer para descobir se ele é primo: '))
if n == 2:
      print(f'O número {n} é primo! ')

for c in range(2, n):
  if n % c == 0:
       print(f'O número {n} não é primo. ')
       break
  elif c == n-1: 
      print(f'O número {n} é primo. ')
