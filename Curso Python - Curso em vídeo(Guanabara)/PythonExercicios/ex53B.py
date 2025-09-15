frase = input('Digite uma frase: ').strip().upper()
palavras = frase.split()
juntas = ''.join(palavras)
inverso = ''
for index_letras in range(len(juntas)-1,-1,-1):
    inverso += juntas[index_letras]
print(juntas, inverso)
if inverso == juntas:
    print('Você tem um palíndromo! ')
else:
    print('A frase em questão, não é um palíndromo. ')
