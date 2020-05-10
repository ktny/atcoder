from heapq import heapify, heappush as hpush, heappop as hpop
N, M, S = map(int, input().split())
k = 2451

X = [[] for _ in range(N * k)]
for _ in range(M):
    u, v, a, b = map(int, input().split())
    u, v = u-1, v-1
    for i in range(a, k):
        X[u * k + i].append([v * k + i - a, b])
        X[v * k + i].append([u * k + i - a, b])

for i in range(N):
    c, d = map(int, input().split())
    for j in range(k - 1):
        X[i * k + j].append([i * k + min(j + c, k - 1), d])

def dijkstra(n, E, i0=0):
    h = [[0, i0]]
    D = [-1] * n
    done = [0] * n
    D[i0] = 0

    while h:
        d, i = hpop(h)
        done[i] = 1
        for j, w in E[i]:
            nd = d + w
            if D[j] < 0 or D[j] > nd:
                if done[j] == 0:
                    hpush(h, [nd, j])
                    D[j] = nd
    return D
 
D = dijkstra(N * k, X, min(S, k - 1))
print(*[min(D[i * k:(i+1) * k]) for i in range(N)][1:], sep = "\n")