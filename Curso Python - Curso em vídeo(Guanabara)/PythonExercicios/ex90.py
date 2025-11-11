aluno = {
    'Nome': input('Nome do aluno: '),
    'Média': float(input('Média do aluno: '))
}

if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado' 
else:
    aluno['Situação'] = 'Reprovado'

print('-'*40)
print(f'O aluno {aluno["Nome"]} foi {aluno["Situação"]} com {aluno["Média"]} de pontuação média. ')
print()
