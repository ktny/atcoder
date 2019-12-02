N = int(input())
S = [input() for i in range(N)]
MARCH = ['M', 'A', 'R', 'C', 'H']
p = {i:0 for i in MARCH}

for i in range(N):
    if S[i][0] in MARCH:
        p[S[i][0]] += 1

from itertools import combinations
ans = 0
for t in combinations(MARCH, 3):
    ans += p[t[0]] * p[t[1]] * p[t[2]]

print(ans)