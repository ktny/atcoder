N = int(input())
A = list(map(int, input().split()))

from functools import lru_cache
@lru_cache(maxsize=None)
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

ans = 1
for i in range(N):
    if i != 0:
        a = A[0]
    else:
        a = A[1]
    for j in range(N):
        if i == j:
            continue
        a = gcd(a, A[j])
    ans = max(ans, a)
print(ans)