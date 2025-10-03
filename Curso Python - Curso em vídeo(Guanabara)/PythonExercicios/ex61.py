print('-='*5, '10 Primeiros Termos De Uma Progressão aritmética', '=-'*5 )
print('Insira os dados progressão: ')

primeiro_termo = int(input('início: '))

razao = int(input('razão: '))

decimo_termo = primeiro_termo

while  decimo_termo != primeiro_termo + razao * 10:
    print(decimo_termo, end=', ')
    decimo_termo += razao
