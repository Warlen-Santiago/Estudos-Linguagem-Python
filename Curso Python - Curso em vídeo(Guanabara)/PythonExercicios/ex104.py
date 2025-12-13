def leiaint(n):
    
    num = input(n)
    while num.isnumeric() == False: 
        print('\n\033[31mErro... O valor inserido é inavlido, tente novamente.\033[m\n ')
        num = input(n)

    return num

n = leiaint('Digite um numero inteiro: ')
 