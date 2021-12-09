import random
SBOX=[[],[],[],[],[],[],[],[]]
a=[]
'''
for i in range(8):
    for j in range(4):
        a=[]
        for k in range(32):
            a.append(k)
        random.shuffle(a)
        print(a)
        SBOX[i].append(a)
    print("")

print(len(SBOX[1][1]))
'''

for i in range(64):
    a.append(i)
    random.shuffle(a)
print(a)