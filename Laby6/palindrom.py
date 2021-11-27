import math

def isPoalindrome(a):
    a = list(a)
    czy_true = ( lambda lista: str(lista).__eq__(str(lista[::-1])))
    print(czy_true(a))

# k a j a k
# k a j   k a j
#isPoalindrome("kajak")
