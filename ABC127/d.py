from collections import defaultdict as dd
N, M = map(int, input().split())
A = list(map(int, input().split()))
BC = [tuple(map(int, input().split())) for i in range(M)]

cards = dd(int)
for a in A:
    cards[a] += 1
for b, c in BC:
    cards[c] += b

ans = 0
for k, v in sorted(cards.items(), key=lambda x: -x[0]):
    if N > v:
        ans += k*v
    else:
        ans += k*N
        break
    N -= v
print(ans)
