times = ('Palmeiras', 'Flamengo', 'Cruzeiro', 'Mirassol', 'Botafogo', 'Bahia', 'Fluminense', 'São Paulo', 'Bragantino', 'Ceará SC', 'Vasco da Gama', 'Corinthians', 'Grêmio', 'Atlético-MG', 'Internacional', 'Santos', 'EC Vitória', 'Fortaleza', 'Juventude', 'Sport Recife')

print(f'{'BRASILEIRÃO 2025':^56}' )
print('-'*50)
print()

for c in times:
    print(c, end=', ')
    
print('\n')
print('-'*50)
print()

print('Os primeiros 5 colocados são: ')

for c in range(0,5):
    print(f'{c+1}° {times[c]}')

print('-'*50)
print()

print('Os 4 ultimos colocados são: ')
for c in range(-1,-5,-1):
    print(f'{c+21}° {times[c]}')

print('-'*50)
print()

t_ordem = sorted(times)

print('Os times participantes em ordem alfabetica são: ')
for c in range(0,20):
    if c <=18:
        print(f'{t_ordem[c]}', end=', ' ) 
    else:
         print(f'{t_ordem[c]}' )

print('-'*50)
print()

print(f'O time do Cruzeiro está em {times.index('Cruzeiro')+1}° lugar e o time do Atlético esta em {times.index('Atlético-MG')+1}°')
print()
