N, M = map(int, input().split())

# 各部品を持っていれば1, 持っていなければ0としたbitの10進数を添字として状態で持つ
dp = [[float('inf') for _ in range(2**N)] for _ in range(M+1)]
# 何も持ってない状態はコスト0
dp[0][0] = 0

for i in range(1, M+1):
    s, c = input().split()
    s = int(s.replace('Y', '1').replace('N', '0'), base=2)
    c = int(c)
    for j in range(2**N):
        # 2次元配列でDPを持つときはsを買わなかったときのdpも埋める
        dp[i][j] = min(dp[i][j], dp[i-1][j])
        dp[i][j|s] = min(dp[i][j|s], dp[i-1][j] + c)

ans = float('inf')
for i in range(1, M+1):
    ans = min(ans, dp[i][-1])

if ans == float('inf'):
    print(-1)
else:
    print(ans)