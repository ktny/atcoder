N, A, B = map(int, input().split())
X = list(map(int, input().split()))

ans = 0
for i in range(N-1):
    d = X[i+1] - X[i]
    if d * A < B:
        ans += d * A
    else:
        ans += B

print(ans)