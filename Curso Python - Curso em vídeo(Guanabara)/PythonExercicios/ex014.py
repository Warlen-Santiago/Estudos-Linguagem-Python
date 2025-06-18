
cel = float(input('Insira um valor em Celsius para converter em Fahrenheit e em Kelvin:\n' ))
fah = cel * (9 / 5) + 32
kel = cel + 273.15
print(f'{cel:.1f}C° é igual a {fah:.1f}F°, que é igual a {kel:.2f}K°' )
