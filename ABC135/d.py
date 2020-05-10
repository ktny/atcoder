S = input()
N = len(S)
mod = 10**9+7
P = 13
 
dp = [[0 for _ in range(P)] for _ in range(N+1)]
dp[0][0] = 1
 
for i in range(N):
    x = S[-1-i]
    if x == '?':
        base = pow(10, i, P)
        for j in range(10):
            r = base*j % P
            for m in range(P):
                dp[i+1][(m+r)%P] = (dp[i+1][(m+r)%P] + dp[i][m]) % mod
    else:
        r = pow(10, i, P) * int(x) % P
        for j in range(P):
            dp[i+1][(j+r)%P] = max(dp[i+1][(j+r)%P], dp[i][j])
 
print(dp[-1][5])
