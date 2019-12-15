N = int(input())
T = [int(input()) for i in range(N)]

from fractions import gcd
def lcm(x, y):
    return (x * y) // gcd(x, y)

ans = 1
for i in range(N):
    ans = lcm(ans, T[i])
print(ans)