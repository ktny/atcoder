N = int(input())
A = list(map(int, input().split()))

ans = [0]*(2**N)
tour = [(i, A[i]) for i in range(2**N)]
r = 1
while N:
    if len(tour) == 2:
        for t in tour:
            ans[t[0]] = r
        break
    wins = []
    for i in range(2**N//2):
        if tour[i*2][1] > tour[i*2+1][1]:
            wins.append((tour[i*2][0], tour[i*2][1]))
            ans[tour[i*2+1][0]] = r
        else:
            wins.append((tour[i*2+1][0], tour[i*2+1][1]))
            ans[tour[i*2][0]] = r
    tour = wins
    N -= 1
    r += 1

print(*ans, sep='\n')