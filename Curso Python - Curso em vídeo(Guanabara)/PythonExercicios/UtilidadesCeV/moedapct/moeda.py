def aumentar(num,perc=10,real=True):
    '''
    Docstring para aumentar
    
    :param num: Descrição
    :param perc: Descrição
    :param real: Descrição
    '''
    perc = perc/100
    aumento_total = num + num*perc

    if real == False:
        return aumento_total
    else:
        return(f'R${aumento_total:.2f} ')


def diminuir(num,perc=10,real=True):
    perc = perc/100
    desconto_total = num - num*perc

    if real == False:
        return desconto_total
    else:
        return(f'R${desconto_total:.2f} ')


def dobro(num,real=True):
    num = num*2

    if real == False:
        return num
    else:
        return(f'R${num:.2f} ')


def metade(num,real=True):
    num = num/2

    if real == False:
        return num
    else:
        return(f'R${num:.2f} ')
    

def resumo(n,a=10,d=10):
    print(f'''
        {real(n)} com aumento de {a}%:     {aumentar(n,a)}
        {real(n)} com desconto de {a}%:    {diminuir(n,d)}
        {real(n)} dobrado:                 {dobro(n)}
        {real(n)} metade:                  {metade(n)}
''')
    

def real(num):
    return(f'R${num:.2f} ')