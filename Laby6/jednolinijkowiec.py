'''
import sys
from collections import Counter
sys.stdin.read()
#lista slow
sys.stdin.read().split()
lambda dlugosc: len(dlugosc)
map(lambda dlugosc: len(dlugosc), sys.stdin.read().split())
# zlicz elementy
Counter(map(lambda dlugosc: len(dlugosc), sys.stdin.read().split()))
#counter tworzy (slownik)
dict(Counter(map(lambda dlugosc: len(dlugosc), sys.stdin.read().split())))

##########################
import sys
import collections

a=dict(collections.Counter(map(lambda dlugosc: len(dlugosc), sys.stdin.read().split())))
print("{",end="")
for k in sorted(a):
    print("%s: %s, " % (k, a[k]),end="") 
print("}")
##########################

python -c 'import sys; from collections import Counter; a=dict(Counter(map(lambda dlugosc: len(dlugosc), sys.stdin.read().split()))); print("{",end=""); [print("%s: %s, " % (k, a[k]),end="") for k in sorted(a)]; print("}")
'''
import sys; from collections import Counter; a=dict(Counter(map(lambda dlugosc: len(dlugosc), sys.stdin.read().split()))); print("{", end=""); [print("%s: %s, " % (k, a[k]),end="") for k in sorted(a)]; print("}")