print(' '*21,'Gerador de PA')
print('-=-'*20)

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
total = primeiro
mais = 0 
repete = 10
cont = 0

while repete+1 >= cont:
    if cont != repete:
        print(total, end=' ⭢ ')
        total += razão
    else:
        mais = int(input('Deseja ver mais, se sim quanto?'))
        repete+=mais+1
        if mais == 0:
            break
    cont+=1
print('Programa encerrado... volte sempre! ')
