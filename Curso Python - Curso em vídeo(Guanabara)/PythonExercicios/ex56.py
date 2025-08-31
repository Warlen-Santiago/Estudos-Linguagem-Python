import numpy as np

nome = []
idade = []
sexo = []

print('Insira Nome, Idade e Sexo( M ou F ) corespondente para cada indivíduo: ')

for c in range(0, 4):
    n = input('Nome: ')
    i = int(input('Idade:'))
    s = input('Sexo: ')

    nome.append(n)
    idade.append(i)
    sexo.append(s.upper())

print(f'A média de idade do grupo é {np.mean(idade)} ')

m_n = []
m_i = []
for c in range(0, 4):
    if sexo[c] == 'M':
        m_n.append(nome[c])
        m_i.append(idade[c])

m_i_m = max(m_i)
i_m_i_m = m_i.index(m_i_m)

print(f'O homen mais velho é {m_n[i_m_i_m]} com {m_i_m} anos. ')

f_mq20 = 0
for c in range(0, 4):
    if sexo[c] == 'F' and idade[c] < 20:
        f_mq20 = f_mq20 + 1
    
print(f'Nesse grupo há {f_mq20} mulher(es) que tem menos de 20 anos. ')