N, W = map(int, input().split())
wv = sorted([list(map(int, input().split())) for i in range(N)], key=lambda x: x[0])

# 重さをi、dp[i]を価値の最大値とする
dp = [0]*(W+1)
dp[0] = 0

for i in range(N):
    w, v = wv[i]
    # 前から埋めていくとさっき更新したやつをもとに更新してしまう（同じものを使ってしまう）ので逆から更新する
    for j in range(W, w-1, -1):
        dp[j] = max(dp[j], dp[j-w] + v)

print(dp[W])