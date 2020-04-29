N = int(input())
A = list(map(int, input().split()))
mod = 10**9+7

from collections import Counter
c = Counter(A)

if N % 2 == 0:
    for i in range(1, N, 2):
        if c[i] != 2:
            break
    else:
        print(2**(N // 2) % mod)
        exit()
    print(0)
else:
    for i in range(0, N, 2):
        if i == 0:
            if c[i] != 1:
                break
        else:
            if c[i] != 2:
                break
    else:
        print(2**(N // 2) % mod)
        exit()
    print(0)
