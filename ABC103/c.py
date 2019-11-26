N = int(input())
A = sorted(list(map(int, input().split())))

from fractions import gcd
def lcm(x, y):
    return (x * y) // gcd(x, y)

m = A[0]
for i in range(1, N):
    m = lcm(m, A[i])
m -= 1

ans = 0
for i in range(N):
    ans += m % A[i]

print(ans)