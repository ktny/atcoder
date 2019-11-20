N = int(input())
V = list(map(int, input().split()))
h = N//2

from collections import Counter
A = Counter(V[::2])
B = Counter(V[1::2])

ac = sorted(A.items(), key=lambda x: -x[1])
bc = sorted(B.items(), key=lambda x: -x[1])

if len(ac) == 1 and len(bc) == 1:
    if ac[0][0] == bc[0][0]:
        print(h)
    else:
        print(0)
elif len(ac) == 1:
    print(h-bc[0][1])
elif len(bc) == 1:
    print(h-ac[0][1])
elif ac[0][0] == bc[0][0]:
    if ac[0][1]-ac[1][1] == bc[0][1]-bc[1][1]:
        if ac[0][1] >= bc[0][1]:
            print((h-ac[0][1]) + (h-bc[1][1]))
        else:
            print((h-ac[1][1]) + (h-bc[0][1]))
    elif ac[0][1]-ac[1][1] > bc[0][1]-bc[1][1]:
        print((h-ac[0][1]) + (h-bc[1][1]))
    else:
        print((h-ac[1][1]) + (h-bc[0][1]))
else:
    print((h-ac[0][1]) + (h-bc[0][1]))