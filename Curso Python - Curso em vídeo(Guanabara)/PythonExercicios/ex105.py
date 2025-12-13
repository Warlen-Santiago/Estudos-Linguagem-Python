def notas(* n, situação=False):
    '''
    Essa função recebe notas de um aluno e armazenas as estatisticas dessas notas em um dicionario, o usuario pode escolher entre aparecer e não a situação atual do aluno com base nas notas
    
    :param n: variavel que recebe as notas do aluno, armazenando todas elas em uma tupla
    :param situação: parametro que permite a escolha da opção de mostrar ou não a situação do aluno
    '''

    relatorio = {
        'Quantidade de notas' : len(n),
        'Maior nota' : max(n),
        'Menor nota' : min(n),
        'Media' : sum(n)/len(n)
    }
    if situação:
        if relatorio['Media'] >= 9:
            relatorio['Situação'] = 'Exelente'
        elif relatorio['Media'] > 7:
            relatorio['Situação'] = 'Boa'
        elif relatorio['Media'] < 7 and relatorio['Media'] > 4.5:
            relatorio['Situação'] = 'na média'
        elif relatorio['Media'] < 4.5:
            relatorio['Situação'] = 'abaixo da média'

    return relatorio

print(notas(10,6.3,5.2,7))
