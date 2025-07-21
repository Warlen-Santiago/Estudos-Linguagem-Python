ano = int(input('Insira um ano para saber se ele é bissexto ou não: '))

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print('Sim, ele é bissexto! ')
        else:
            print('Não, ele não é bissexto! ')
    else:
        print('Sim, ele é bissexto! ')
else:
    print('Ele não é bissexto! ')
