N, Q = map(int, input().split())
S = [list(map(int, input().split())) for i in range(Q)]

ans = [['N']*(N+1) for i in range(N+1)]

for i in range(Q):
    s = S[i]
    if s[0] == 1:
        a = s[1]
        b = s[2]
        ans[a][b] = 'Y'
    elif s[0] == 2:
        a = s[1]
        for x in range(1, N+1):
            if x == a:
                continue
            if ans[x][a] == 'Y':
                ans[a][x] = 'Y'
    elif s[0] == 3:
        a = s[1]
        tmp = set()
        for x in range(1, N+1):
            if x == a:
                continue
            if ans[a][x] == 'Y':
                tmp.add(x)
        for x in range(1, N+1):
            if x == a:
                continue
            if x in tmp:
                for f in range(1, N+1):
                    if a == f:
                        continue
                    if ans[x][f] == 'Y':
                        ans[a][f] = 'Y'

for i in range(1, N+1):
    for j in range(1, N+1):
        print(ans[i][j], sep='', end='')
    print()