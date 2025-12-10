def fatorial(n,show=True):
    '''
    Docstring para fatorial
    o fatorial de um número inteiro positivo n é o produto(multiplicação) de todos os números inteiros positivos menores ou iguais a n
    essa função retorna o produto do fatorial do numero escolhido e te da a opção de mostrar ou não na tela o processo para chegar a tal
    :param n: recebe o numero inteiro possitivo que sera feita a equação
    :param show: parametro de escolha se sera ou não mostrado o processo da equação 
    '''
    resul = 1
    for c in range(1,n+1):
        if show:
            print(f'{resul} x {c} =',end=' ') 

        resul = resul * c
        if show:
            print(f'{resul}')
        
    return resul

print(fatorial(5))