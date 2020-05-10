N = int(input())
tasks = [[] for _ in range(N)]
for i in range(N):
    a, b = map(int, input().split())
    tasks[a-1].append(b)

from heapq import heapify, heappop, heappush
points = []
heapify(points)

ans = 0
for i in range(N):
    for t in tasks[i]:
        heappush(points, -t)
    p = heappop(points)
    ans -= p
    print(ans)
