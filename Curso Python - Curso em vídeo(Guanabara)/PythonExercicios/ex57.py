sexo = ''
while sexo not in ['M', 'F']:
    sexo = input('Insira seu sexo[M/F]: ').upper().strip()
    if sexo not in ['M', 'F']:
        print('Insira uma opção valida e tente novamente. ')
print('Sexo inserido com sucesso. ')
