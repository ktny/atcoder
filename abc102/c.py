N = int(input())
A = list(map(int, input().split()))

minv = min(A)
maxv = max(A)
ans = (-1, float('inf'))
for b in range(maxv+1):
    t = 0
    for i in range(N):
        t += abs(A[i] - (b+i+1))
    print(b, t)
    if ans[1] > t:
        ans = (b, t)
print(ans)