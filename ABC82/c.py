N = int(input())
A = sorted(list(map(int, input().split())))
ans = 0
from itertools import groupby
for k, v in groupby(A):
    c = 0
    for i in v:
        c += 1
    if k > c:
        ans += c
    elif k < c:
        ans += c-k
print(ans)