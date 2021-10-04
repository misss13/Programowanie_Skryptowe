from fractions import Fraction


def sum(arg1, arg2):
    #ułamki
    if type(arg1) == type(Fraction(1,2)) or type(arg2) == type(Fraction(1,2)):
        return arg1+arg2
    #zespolone
    if type(arg1) is complex or type(arg2) is complex:
        return complex( arg1.real+arg2.real, arg1.imag+arg2.imag )
    #float otaz str
    assert float(arg1), "Błąd, to nie liczba"
    assert float(arg2), "Błąd, to nie liczba"
    a1=float(arg1)
    a2=float(arg2)
    return a1+a2


if __name__ == '__main__':
    a=2
    b=2
    print("suma = ", sum(a, b))
    print("__name__ = ", __name__)