N = int(input())
A = list(map(int, input().split()))

ans = float('inf')
for i in range(-100, 101):
    tmp = 0
    for j in range(N):
        tmp += (A[j] - i)**2
    if ans > tmp:
        ans = tmp

print(ans)