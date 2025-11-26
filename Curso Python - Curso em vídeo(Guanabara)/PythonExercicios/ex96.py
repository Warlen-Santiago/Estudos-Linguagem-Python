def area(l, c):
    print(f'A área total do terreno é de {l * c:.2f} metros quadrados. ')

def linha():
    print('-'*50)

linha()
print('Calculando a área de um terreno: ')
linha()

largura = float(input('  Insira a largura do terreno: '))
comprimento = float(input('  Insira o comprimento do terreno: '))

linha()

area(largura, comprimento)
print()