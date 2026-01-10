def maiusculo(txt):
    return txt.upper()
    

def minusculo(txt):
    return txt.lower()
    

def contar_caracteres(txt):
    lista = txt.split()
    txt = ''.join(lista)
    quant = len(txt)
    return quant