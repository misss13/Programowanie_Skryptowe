# Python code to illustrate
# Decorators with parameters in Python
'''
from collections import Counter
import sys
from collections import defaultdict

a=dict(Counter(map(lambda x: len(x), sys.stdin.read().split())))
print(a)
b=defaultdict(list)
for k, v in a.items():
    b[v].append(k)
print(dict(b))'''

