def ficha(nome='(desconhecido)',gols=0):
    print(f'O jogador {nome} marcou {gols} gol(s) até o momento. ')

def escreva(txt):
    q = len(txt)
    print('-'*(q+2))
    print(f' {txt} ')
    print('-'*(q+2))
    print()


escreva('FICHA DOS JOGARES')
n = input('Nome: ').capitalize()
g = input('Quantos gols ele marcou: ')

print('-'*20)

if g.isnumeric():
    g = int(g)
else:
    g = 0

if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n,g)

print()
