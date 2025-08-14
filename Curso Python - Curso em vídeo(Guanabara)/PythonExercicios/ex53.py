import unicodedata

def remove_acentos(string):
    forma_normalizada = unicodedata.normalize('NFKD', string)
    para_ascii = forma_normalizada.encode('ascii', 'ignore')
    string_sem_acentos = para_ascii.decode('ascii')
    return string_sem_acentos

print('-='*5,'Descobrindo de uma frase é ou não palíndromo', '=-'*5 )
print('EX: "A mala nada na lama." a frase permanece a mesma se lida de trás pra frente desconsiderando espaços e etc. ')
frase = input('Insira sua frase para conferir: ').strip()

frase = remove_acentos(frase)

frase2 = frase.split()

frase = ''.join(frase2).lower()

n = len(frase)

e_palindromo = True

for c in range(0, n//2):
    if frase[c] != frase[n-1-c]:
        e_palindromo = False
        break

if e_palindromo:
    print('Sim, sua frase é um palíndromo.')
else:
    print('Não, sua frase não é um palíndromo.')
