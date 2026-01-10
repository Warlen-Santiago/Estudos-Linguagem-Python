def leiavalores(v):
    txt = v
    while True:
        v = input(txt).strip()

        if v.isnumeric():
            v = int(v)
            return v 
            break

        else:
        
            if v.count('.') == 1: 
                v1 = v.replace('.','')

                if v1.isnumeric():
                    v = float(v)
                    return v
                    break
                else:
                    print('\033[;31mO valor inserido é invalido, insira outro valor e tente novamente\033[m')

            elif v.count(',') == 1:
                v1 = v.replace(',','')

                if v1.isnumeric():
                    v = v.replace(',','.')
                    v = float(v)
                    return v
                    break
                else:
                    print('\033[;31mO valor inserido é invalido, insira outro valor e tente novamente\033[m')
            else:
                print('\033[;31mO valor inserido é invalido, insira outro valor e tente novamente\033[m')

