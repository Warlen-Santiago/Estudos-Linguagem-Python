from pct115 import txt, dados, valide # importando os modulos, apesar de poder importar somente o pacote por questões de organização e legibilidade prefri importar direto do camiho
from time import sleep

txt.cor('azul')
txt.titulo('- Cadastro de pessoas -')# iulo inicial
txt.cor()

# buscano se ja ha uma lista com pessoas cadastradas ou se é preciso criar uma 
pessoas = dados.carrega('lista_de_pessoas.json')

while True:

    txt.cor('cinza')
    escolha_menu = valide.valida('''                     
        - opções
                    
          1 - Ver dados cadastrados
          2 - Cadastrar uma pessoa
          3 - Fechar programa

                                   
----------------------------------------------------------------------------------------------------
''',(1, 2, 3)) # Menu com as devidas pções
    
    if escolha_menu == 1: # Escolha numero 1 do menu
        sleep(0.5)
        if pessoas:
            
            txt.cor('roxo')
            txt.titulo('Dados cadastrados: ')
            
            for p in pessoas:
                print(f'Nome: {p['Nome']:<50} - Idade: {p['Idade']} ') # Mostrando os dados cadastrados
            print('-'*100)
            txt.cor()
            
        else:

            txt.cor('verde')
            txt.titulo('Não há nenhuma pessoa cadastrada, caso deseje cadastrar escolha a opção 2. ') # informando caso não haja dados cadastrados
            txt.cor()

    elif escolha_menu == 2: # Escolha numero 2 do menu
        sleep(0.5)

        txt.cor('verde')
        txt.titulo('Cadastrando...')
        txt.cor()


        nome = valide.validastr('Nome: ')
        idade = valide.validaint('Idade: ') # coletando dados

        pessoa = {
            'Nome' : nome.capitalize(), # organizando os dados coletados em um dict
            'Idade' : idade
        }

        pessoas.append(pessoa) # passando dict para lista

        dados.salva('lista_de_pessoas.json', pessoas) # salva os dados

        print('-'*100)

    elif escolha_menu == 3: # Escolha numero 3 do menu
        sleep(0.5)

        txt.cor('Azul')
        txt.titulo('Programa encerrado... volte sempre!') # mensagem de encerramento
        txt.cor()
        print('\n')

        break
    sleep(2)
        