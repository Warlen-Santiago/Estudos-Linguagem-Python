numeros = 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'

escolha = 22
while escolha > 20 or escolha < 0 :
    escolha = int(input('Escolha um número inteiro de 1 a 20: '))
    print()

    if 0<=escolha<=20:
        print(f'O número {escolha}, por extenso é {numeros[escolha-1]}. ')
        print()
