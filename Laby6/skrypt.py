
import itertools, functools, sys, re

a =  map(lambda plik: open(plik, 'r').read(), sys.argv[1:])
a = list(a)
a = functools.reduce(lambda b, c: b + c, a)
a = re.findall( r'\d+', a)
a = list(a)
a = list(filter(lambda liczba: int(liczba) % 2 == 0, a))
a = len(a)
print(a)

'''
import itertools, functools, sys, re

a=len(
    list(
        filter(
            lambda liczba: int(liczba) % 2 == 0,
            list(
                re.findall( r'\d+',
                    functools.reduce( lambda b, c: b + c,
                        list(
                            map( lambda x: open(x, 'r').read(), sys.argv[1:])
                            )
                        )
                    )
                )
            )       
        )
    )
print(a)
'''