posicao = int(input("Digite a posição desejada na sequência de Fibonacci (1°, 2°, 3°, etc.): "))


# Calculando o número na posição 
if posicao == 1:
    resultado = 0

elif posicao == 2:
    resultado = 1

else:
    a, b = 0, 1
    contador = 2  # Já sabemos as duas primeiras posições
    
    while contador < posicao:
        a, b = b, a + b
        contador += 1
    
    resultado = b

print(f"O {posicao}° número da sequência de Fibonacci é: {resultado}")
