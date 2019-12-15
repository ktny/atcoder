N = int(input())
A = list(map(int, input().split()))
mod = 10**9+7
ans = 0

for k in range(60):
    zero = 0
    one = 0
    for i in range(N):
        # A[i]のk桁目のbitが0か1か取り出す
        x = (A[i] >> k) & 1
        if x == 0: zero += 1
        else: one += 1
    ans += (2**k * (zero * one)) % mod

print(ans % mod)