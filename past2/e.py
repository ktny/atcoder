N = int(input())
A = list(map(int, input().split()))

ans = []
for i in range(1, N+1):
    cnt = 1
    x = i
    tmp = x
    while x != A[tmp-1]:
        tmp = A[tmp-1]
        cnt += 1
    ans.append(cnt)

print(*ans)