def leiaint(n):
    while True:
        try:
            num = int(input(n))
        except ValueError:
            print('\033[31mO tipo de dado inserido é invalido... Insira um dado valido e tente novamente\033[m\n ')
        except KeyboardInterrupt:
            print('\033[31mO usuario interrompeu a execução do programa...\033[m\n')
            break
        else:   
            return num
            


def leiavalores(v):
    txt = v
    while True:
        try:
            v = input(txt).strip()

            if v.isnumeric():
                v = int(v)
                return v 
                

            else:
            
                if v.count('.') == 1: 
                    v1 = v.replace('.','')

                    if v1.isnumeric():
                        v = float(v)
                        return v
                        
                    else:
                        print('\033[;31mO valor inserido é invalido, insira outro valor e tente novamente\033[m')

                elif v.count(',') == 1:
                    v1 = v.replace(',','')

                    if v1.isnumeric():
                        v = v.replace(',','.')
                        v = float(v)
                        return v
                        
                    else:
                        print('\033[;31mO valor inserido é invalido, insira outro valor e tente novamente\033[m')
                else:
                    print('\033[;31mO valor inserido é invalido, insira outro valor e tente novamente\033[m')
        except KeyboardInterrupt:
            print('\033[;31mO usuario interrompeu o programa...\033[m ')
            return 0
            break
                    