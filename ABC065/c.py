N, M = map(int, input().split())
mod = 10**9+7

def f(n):
    ret = 1
    for i in range(1, n+1):
        ret = (ret * i) % mod
    return ret

if abs(N-M) > 1:
    print(0)
elif N == M:
    print(f(N)**2*2 % mod)
else:
    a = N if N > M else M
    print(f(a)*f(a-1) % mod)
