from fractions import gcd
N, X = map(int, input().split())
xs = list(map(int, input().split()))
xs.append(X)
xs.sort()
ds = [xs[i+1]-xs[i] for i in range(N)]
ans = ds[0]
for i in range(1, N):
    ans = gcd(ans, ds[i])
print(ans)