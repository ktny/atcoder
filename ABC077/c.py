N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
C = sorted(list(map(int, input().split())))

from bisect import bisect_left, bisect_right
ans = 0
for b in B:
    ai = bisect_left(A, b)
    ci = bisect_right(C, b)
    ans += ai * (N-ci)
print(ans)