frase = input('Insira uma frase qualquer: ').upper().strip()

print(f'Nessa frase a letra A apareceu um total de: {frase.count('A')} vezes. ')

print(f'A letra A aparece pela primeira vez na casa {frase.find('A') + 1} isso contando os espaços. ')

print(f'A letra A aparece pela ultima vez na casa {frase.rfind('A') + 1} isso contando os espaços. ')

