N, K = map(int, input().split())
A = list(map(int, input().split()))
mod = 10**9+7

ans = 0
tmp = 0
tmp2 = 0
for i in range(N):
    for j in range(i):
        if A[i] < A[j]:
            tmp += 1
    for j in range(N):
        if A[i] > A[j]:
            tmp2 += 1

k = (K * (K-1) // 2) % mod
ans = ans + (tmp * K % mod) + (tmp2 * k % mod)
print(ans % mod)
