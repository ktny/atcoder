N = int(input())
mod = 10**9+7

def factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

from collections import defaultdict as dd

d = dd(int)

for i in range(1, N+1):
    a = factorize(i)
    for j in a:
        d[j] += 1

ans = 1
for k, v in d.items():
    ans = ans * (v+1) % mod
print(ans)
