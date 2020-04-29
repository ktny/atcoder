H, W = map(int, input().split())
N = int(input())
A = list(map(int, input().split()))

g = [[0 for _ in range(W)] for _ in range(H)]
h = 0
w = 0
for i in range(1, N+1):
    for _ in range(A[i-1]):
        g[h][w] = i
        if h % 2 == 0:
            w += 1
            if w > W-1:
                h += 1
                w = W-1
        else:
            w -= 1
            if w < 0:
                h += 1
                w = 0

for i in range(H):
    print(*g[i])
