def escreva(txt):
    q = len(txt)
    print('-'*(q+2))
    print(f' {txt} ')
    print('-'*(q+2))
    print()

esc = input('Insira um texto: ').upper()
print()

escreva(esc)