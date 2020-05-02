N, K = map(int, input().split())

ans = 0
# bを固定して考える
for b in range(K+1, N+1):
    tmp = 0
    q, r = divmod(N+1, b)
    tmp += q * (b-K)
    if r > K:
        tmp += r - K
    if K == 0:
        tmp -= 1
    ans += tmp
print(ans)
