N, K = map(int, input().split())
H = list(map(int, input().split()))

# 各足場までのコストの最小値のリスト
dp = [float('inf')] * N
dp[0] = 0
for i in range(N):
    for j in range(K+1):
        if i-j >= 0:
            dp[i] = min(dp[i], dp[i-j]+abs(H[i]-H[i-j]))
print(dp[-1])