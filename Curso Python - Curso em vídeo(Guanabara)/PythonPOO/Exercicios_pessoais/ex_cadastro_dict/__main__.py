from rich import print

print(f'{50*'-'}')
pessoa1 = {
    'nome' : input('Qual seu nome? ').strip().capitalize(),
    'idade' : int(input('Qual sua idade? ')),
    'altura' : float(input('Qual sua altura? ')),
    'peso' : float(input('Qual seu peso? ')),
    'trabalha' : input('Trabalha[S/N]').strip().upper()
}
while pessoa1['trabalha'] not in ['S','N']:
    pessoa1['trabalha'] = input('Trabalha[S/N]').strip().upper()
print(f'{50*'-'}')

if pessoa1['trabalha'] == 'S':
    pessoa1['trabalha'] = True
else:
    pessoa1['trabalha'] = False


print(f'Seu nome é {pessoa1["nome"]}, você tem {pessoa1["idade"]} anos, pesa {pessoa1["peso"]:.2f}Kg e sua altura é {pessoa1["altura"]:.2f} e atualmente você { "trabalha" if pessoa1["trabalha"] else "Não Trabalha" }\n')

