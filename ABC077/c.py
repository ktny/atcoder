N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
C = sorted(list(map(int, input().split())))

from bisect import bisect_left

mids = []
for b in B:
    ind = bisect_left(A, b)
    mids.append(ind)
cs = [0]
for i in range(N):
    cs.append(cs[i]+mids[i])
ans = 0
for c in C:
    ind = bisect_left(B, c)
    ans += cs[ind]
print(ans)
