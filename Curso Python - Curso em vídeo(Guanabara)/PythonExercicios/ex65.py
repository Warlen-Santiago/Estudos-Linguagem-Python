n=0
list_n=[]
escolha = ''

while escolha != 'N':
    n = int(input(f'insira um número inteiro: '))
    list_n.append(n)
    escolha = input('Você deseja continuar?[S/N] ').upper().strip()
    

print()
print(f'A média entre os números inseridos é {sum(list_n)/len(list_n):.0f}. ')
print(f'O maior número inserido foi {max(list_n)}. ')
print(f'O menor número inserido foi {min(list_n)}. ')
