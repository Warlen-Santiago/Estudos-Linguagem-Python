print('Calculando situação do aluno: ')
n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))

med = (n1+n2)/2

if med < 5:
    print('Você foi reprovado, se dedique mais na proxima vez! ')
elif med > 5 and med < 6.9:
    print('Você ficou de recuperação, estude bastante para a prova! ')
else:
    print('Você foi aprovado parabéns! \U0001f973 ')
