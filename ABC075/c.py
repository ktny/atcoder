N, M = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(M)]

def bfs(n, t, v):
    for p in t[n]:
        if p not in visited:
            visited.add(p)
            bfs(p, t, v)

ans = 0
for i in range(M):
    t = {i:[] for i in range(1, N+1)}
    visited = set()
    for j in range(M):
        if i == j:
            continue
        a, b = ab[j]
        t[a].append(b)
        t[b].append(a)
    bfs(1, t, visited)
    if len(visited) != N:
        ans += 1

print(ans)