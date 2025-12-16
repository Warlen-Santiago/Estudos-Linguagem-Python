def aumentar(num,perc=10):
    perc = perc/100
    aumento_total = num + num*perc

    return aumento_total


def diminuir(num,perc=10):
    perc = perc/100
    desconto_total = num - num*perc

    return desconto_total


def dobro(num):
    num = num*2

    return num


def metade(num):
    num = num/2

    return num 