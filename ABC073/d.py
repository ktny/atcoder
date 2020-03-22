N, M, R = map(int, input().split())
r = list(map(int, input().split()))
ABC = [list(map(int, input().split())) for i in range(M)]

dist = [[float('inf') for _ in range(N+1)] for _ in range(N+1)]

for i in range(N+1):
    dist[i][i] = 0
for a, b, c in ABC:
    dist[a][b] = c
    dist[b][a] = c

# ワーシャルフロイドで各頂点ごとの最短距離を求める
for k in range(N+1):
    for i in range(N+1):
        for j in range(N+1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

from itertools import permutations as per

ans = float('inf')
for k in per(r, R):
    score = 0
    for i in range(R-1):
        score += dist[k[i]][k[i+1]]
    ans = min(ans, score)

print(ans)
