N = int(input())
xyh = sorted([list(map(int, input().split())) for i in range(N)], key=lambda x: -x[2])

from itertools import product
for cx, cy in product(range(101), repeat=2):
    H = None
    for x, y, h in xyh:
        if H is None:
            H = h + abs(x-cx) + abs(y-cy)
        else:
            if h != max(H - abs(x-cx) - abs(y-cy), 0):
                break
    else:
        print(cx, cy, H)
        exit()