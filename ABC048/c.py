N, x = map(int, input().split())
A = list(map(int, input().split()))

B = [A[0]]
for i in range(N-1):
    B.append(A[i] + A[i+1])
B.append(A[-1])

ans = 0
for i in range(N+1):
    if B[i] > x:
        a = B[i] - x
        ans += a
        B[i] -= a
        if i < N:
            B[i+1] -= a
print(ans)