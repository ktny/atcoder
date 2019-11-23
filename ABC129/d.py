H, W = map(int, input().split())
S = [input() for _ in range(H)]
L, R, U, D = [[[0]*W for _ in range(H)] for i in range(4)]

for h in range(H):
    for w in range(W):
        if S[h][w] == '.':
            L[h][w] = L[h][w-1]+1
            U[h][w] = U[h-1][w]+1
        if S[h][W-1-w] == '.':
            R[h][-w-1] = R[h][-w]+1
        if S[H-1-h][w] == '.':
            D[-h-1][w] = D[-h][w]+1

ans = 0
for i in range(H):
    for j in range(W):
        light = L[i][j] + R[i][j] + U[i][j] + D[i][j] - 3
        ans = max(ans, light)

print(ans)
