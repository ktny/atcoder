N, Q = map(int, input().split())

ans = [['N']*(N+1) for i in range(N+1)]
follower = [[] for i in range(N+1)]
followee = [[] for i in range(N+1)]

for _ in range(Q):
    s = list(map(int, input().split()))
    if s[0] == 1:
        a = s[1]
        b = s[2]
        ans[a][b] = 'Y'
        follower[b].append(a)
        followee[a].append(b)
    elif s[0] == 2:
        a = s[1]
        for f in follower[a]:
            ans[a][f] = 'Y'
            follower[f].append(a)
            followee[a].append(f)
    elif s[0] == 3:
        a = s[1]
        for x in followee[a][:]:
            for f in followee[x]:
                ans[a][f] = 'Y'
                follower[f].append(a)
                followee[a].append(f)

for i in range(1, N+1):
    for j in range(1, N+1):
        print(ans[i][j], sep='', end='')
    print()