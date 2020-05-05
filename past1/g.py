N = int(input())

g = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(1, N):
    A = list(map(int, input().split()))
    for j in range(N-i-1, -1, -1):
        g[i][j+i+1] = A[j]

def Base_10_to_n(X, n):
    if (int(X/n)):
        return Base_10_to_n(int(X/n), n)+str(X%n)
    return str(X%n)

ans = -1*float('inf')
for num in range(3**N):
    tmp = 0
    tri = Base_10_to_n(num, 3).zfill(N)
    groups = [[],[],[]]
    for i,t in enumerate(tri):
        t = int(t)
        groups[t].append(i+1)
    for group in groups:
        l = len(group)
        for i in range(l):
            for j in range(i+1, l):
                tmp += g[group[i]][group[j]]
    ans = max(ans, tmp)
print(ans)