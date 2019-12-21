N = int(input())
A = sorted(list(map(int, input().split())))

from collections import Counter
c = Counter(A)
w = 0
h = 0
for k, v in sorted(c.items(), key=lambda x: -x[0]):
    if v >= 4:
        if w == 0:
            w = h = k
            break
        else:
            h = k
            break
    elif v >= 2:
        if w == 0:
            w = k
        elif h == 0:
            h = k
            break
print(w*h)