#-*-coding: utf-8-*-

if __name__=="__main__":
    #2. 3.
    lancuch1='''Ala 
ma
królika'''
    lancuch2='''Gośka
je
barszcz'''

    print((lancuch1+lancuch2)*3)
    print()

    #4. 5.
    lancuch="Lorem ipsum"
    print(lancuch[0])
    print(lancuch[:2])
    print(lancuch[2:])
    print(lancuch[-2])
    print(lancuch[-3:])
    print(lancuch[::2])
    print()

    #6. nie można było w tekscie
    try:
        lancuch[0]='l'
    except:
        print("Nie da się")

