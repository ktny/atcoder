N, M = map(int, input().split())

from fractions import gcd

def make_divisors(n: int):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors

divisors = make_divisors(M)

ans = 0
for i in range(len(divisors)):
    d = divisors[i]
    if d*(N-1) >= M:
        continue
    ans = max(ans, gcd(d, M-(d*(N-1))))

print(ans)

