Q = int(input())

from functools import lru_cache
@lru_cache(maxsize=None)
def is_prime(n: int):
    if n == 2:
        return True
    if n == 1 or n % 2 == 0:
        return False
    for p in range(3, int(n**0.5)+1, 2):
        if n % p == 0:
            return False
    return True

like_2017s = []
for i in range(3, 10**5, 2):
    if is_prime(i) and is_prime((i+1)//2):
        like_2017s.append(i)

from bisect import bisect_left, bisect_right
for _ in range(Q):
    l, r = map(int, input().split())
    li = bisect_left(like_2017s, l)
    ri = bisect_right(like_2017s, r)
    print(ri-li)