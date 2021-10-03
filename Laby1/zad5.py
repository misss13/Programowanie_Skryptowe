import sys


def Pierwsza(licz):
    if licz == 2 or licz == 1:
        return True
    for i in range(2, (licz//2) + 1):
        if licz % i == 0:
            return False
    return True


if __name__ == "__main__":
    for arg in sys.argv[1::]:
        a=int(arg)
        if Pierwsza(a) == True:
            print(a)