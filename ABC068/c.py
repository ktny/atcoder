N, M = map(int, input().split())
ab = sorted([list(map(int, input().split())) for i in range(M)], key=lambda x: x[0])

t = {i:[] for i in range(1,N+1)}
for a, b in ab:
    if a == 1:
        t[a].append(b)
    elif b == N:
        t[a].append(N)

for i in t[1]:
    if len(t[i]) == 1:
        print('POSSIBLE')
        exit()
else:
    print('IMPOSSIBLE')
