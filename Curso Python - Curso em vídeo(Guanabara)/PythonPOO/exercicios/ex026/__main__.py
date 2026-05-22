from rich import print
import lib as l

def main():
    func1 = l.Horista('Marcelo Coelho', 80, 20)
    func1.calc_sal()
    print(func1.analisar_sal())

    fun2 = l.Mensalista('Sebastian', 3700)
    fun2.calc_sal()
    print(fun2.analisar_sal())

if __name__ == '__main__':
    main()