print('Calculando a quantidade de tinta gasta para pintar uma parede.' )

lar = float(input('Qual a largura da parede?\n' ))
alt = float(input('Qual a altura da parede?\n' ))

are = alt * lar

print(f'A área da parede é de {are:.2f}m^2' )
print(f'Será necessario {are/2:.2f}L de tinta para a pintura.' )