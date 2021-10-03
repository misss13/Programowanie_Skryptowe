import main
import cmath
from fractions import Fraction




def contains_letter(stri):
    for i in stri:
        if i.isalpha():
            return 1 #zawiera litery
        if i == " " or i == ":" or i == ";" or i == "\'" or i == "\"" or i =="?" or i == "\/":
            return 1 #zawiera znaki specjalne
    return 0 #niezawiera liter


def sum(arg1, arg2):
    if type(arg1) == type(1) and type(arg2) == type(1):
        return arg1+arg2
    if type(arg1) == type(1.0) and type(arg2) == type(1.0):
        return arg1+arg2
    if type(arg1) == type(1) and type(arg2) == type(1.0):
        return arg1+arg2
    if type(arg1) == type(1.0) and type(arg2) == type(1):
        return arg1+arg2
    if type(arg1) == type(Fraction(1,2)) and type(arg2) == type(Fraction(1,2)):
        return float(arg1+arg2)
    if type(arg1) is complex or type(arg2) is complex:
        return complex( arg1.real + arg2.real, arg1.imag + arg2.imag )
    
    if type(arg1) == type(Fraction(1,2)):
        arg1=float(arg1)
    if type(arg2) == type(Fraction(1,2)):
        arg2=float(arg2)

    if type(arg1) == type("aa"):
        if contains_letter(arg1) == 1:
            arg1="0"
        if arg1.find(".") != -1:
            arg1=float(arg1)
        else:
            arg1=int(arg1)
    if type(arg2) == type("aa"):
        if contains_letter(arg2) == 1:
            arg2="0"
        if arg2.find(".") != -1:
            arg2=float(arg2)
        else:
            arg2=int(arg2)
    return arg1+arg2


if __name__ == '__main__':
    a=2
    b=2
    print("suma = ", sum(a, b))
#print("__name__ = ", __name__)