print('-='*5, 'Progressão aritmética', '=-'*5 )
print('Insira o lapso de némeros em que ocorrerá a progressão: ')
n1 = int(input('início: '))
n2 = int(input('fim: '))
n3 = int(input('Insira o intervalo em que os números se repetirão: '))

for c in range(n1-n3, n2, n3):
    print(c+n3)
