from math import sin, cos, tan, radians

graus = float(input('Insira um ângulo em Graus Para ser calculado o seno cosseno e tangente.\n '))

rad = radians(graus)
seno = sin(rad)
cosseno = cos(rad)
tangente = tan(rad)

print(f'O seno é: {seno:.2f}\nO cosseno é: {cosseno:.2f}\nE a tangente é: {tangente:.2f} ')