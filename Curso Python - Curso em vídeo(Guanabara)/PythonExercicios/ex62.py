print('-='*5, 'Termos De Uma Progressão aritmética', '=-'*5 )
print('Insira os dados da progressão: ')

primeiro_termo = int(input('início: '))

razao = int(input('razão: '))

decimo_termo = primeiro_termo

while  decimo_termo != primeiro_termo + razao * 10:
    print(decimo_termo)
    decimo_termo += razao

ver_mais = 1
while decimo_termo != primeiro_termo + razao * (10 + ver_mais):
    ver_mais = int(input('Você gostaria de ver mais termos, se sim quantos?(se não, insira 0 para encerrar): '))

    if ver_mais != 0:
        while decimo_termo != primeiro_termo + razao * (10 + ver_mais):
            print(decimo_termo)
            decimo_termo += razao
        ver_mais += 1

print('Programa encerrado. ')

