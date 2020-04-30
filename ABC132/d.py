N, K = map(int, input().split())
mod = 10**9+7

def modinv(a, mod=10**9+7):
    return pow(a, mod-2, mod)

def combination(n, r, mod=10**9+7):
    r = min(r, n-r)
    res = 1
    for i in range(r):
        res = res * (n-i) * modinv(i+1, mod) % mod
    return res

for i in range(1, K+1):
    if N-K+1 < i:
        print(0)
    else:
        print((combination(N-K+1, i) * combination(K-1, i-1)) % mod)