N = int(input())
A = list(map(int, input().split()))

B = [0]
for i in range(N):
    B.append(B[i]+A[i])

ans = float('inf')
for i in range(1, N):
    ans = min(ans, abs((B[-1]-B[i])-B[i]))
print(ans)