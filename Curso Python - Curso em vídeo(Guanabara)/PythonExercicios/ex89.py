from time import sleep
print(f'{'NOTAS DOS ALUNOS':^50}')
print('-'*50)

dados = []#armazena os dados de todos os alunos
aluno = []#recebe o nome do aluno e a lista de notas, que sera passado para a lista dados
notas = []#recebe as notas dos alunos que serão passadas para a lista aluno

while True:
    aluno.append(input('Nome do aluno: '))

    for c in range(0,4):
        notas.append(float(input(f'{c+1}° nota: ')))

    #anexando uma copia dos dados de uma lista para outra
    aluno.append(notas[:])
    dados.append(aluno[:])

    #limpando as listas ao final do ciclo para receber novos dados quando ele se repetir
    notas.clear()
    aluno.clear()

    #conferindo se há mais alunos a serem cadastrados 
    escolha = ''
    while escolha not in ('N', 'S'):
        escolha = input('Você deseja continuar?[S/N] ')[0].upper().strip()
    if escolha == 'N':
        break
    print()

print('-'*50)

#Mostrando os dados coletados
print(f'N°.Nome{'Med.Notas':>24}')
for n, c in enumerate(dados):
    print(f'''{n+1}.{c[0]:<15}{sum(c[1])/4:>10.1f} ''')

print('-'*50)

#loop para mostrar as notas dos alunos
escolha = 0
while escolha != 999:
    escolha = int(input('''Deseja mostrar as notas de qual aluno: 
[N°. referente a tabela/999 encerra]\n '''))
    print('-'*50)

    if escolha != 999:

        #timer e printe para etetica geral do codigo
        sleep(0.5)
        print()

        print(f'As notas de {dados[escolha-1][0]} são: {dados[escolha-1][1]}')

        print()
        sleep(0.5)
    else:
        print('Programa encerrado, volte sempre! ')

    print('-'*50)
    sleep(1)

print()
