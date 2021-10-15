

if __name__=="__main__":
    zawartosc=[]
    zawartosc=(input("Podaj księgozbiór: ").replace(" ", "")).split(sep=",")
    print(zawartosc)
    zawartosc_ksiegozbioru = [[0 for x in range(2)] for y in range(len(zawartosc))]
    for i in range(len(zawartosc)):
        zawartosc_ksiegozbioru[i] = zawartosc[i].split(sep=":")
        try:
            zawartosc_ksiegozbioru[i][1]=int(zawartosc_ksiegozbioru[i][1])
        except:
            print("Prosze podać liczę książek a nie litery!!! Podawanie jeszcze raz")
            i=0
    print(zawartosc_ksiegozbioru)
    operacje= []
    while True:
        try:
            b=input()
            operacje.append(b)   
        except EOFError:
            break
    print(operacje)