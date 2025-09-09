print('-='*5, '10 Primeiros Termos De Uma Progressão aritmética', '=-'*5 )
print('Insira os dados progressão: ')
primeiro_termo = int(input('início: '))
razao = int(input('razão: '))
decimo = primeiro_termo + (10-1) * razao
for c in range(primeiro_termo-razao,decimo, razao):
    print(c+razao)
