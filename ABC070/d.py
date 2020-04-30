import sys
sys.setrecursionlimit(500000)

import sys
def input():
    return sys.stdin.readline()[:-1]

N = int(input())

tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b, c = map(int, input().split())
    tree[a].append((b, c))
    tree[b].append((a, c))

Q, K = map(int, input().split())

def dfs(start, dist, dists, f=None):
    for n, d in tree[start]:
        if n == f:
            continue
        dists[n] = dist + d
        dfs(n, dist+d, dists, start)

xy = [list(map(int, input().split())) for i in range(Q)]

dists = [0] * (N+1)
dfs(K, 0, dists)

for i in range(Q):
    x, y = xy[i]
    print(dists[x] + dists[y])
