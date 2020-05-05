N, K = map(int, input().split())
mod = 10**9+7

# すべての要素がiの倍数であるような数列の数
# 後ろから確定して引いていく。前からだと重複が入ってあとから引きづらくなる
m = [0] * (K+1)
for i in range(K, 0, -1):
    m[i] = pow(K//i, N, mod)
    j = 2
    while True:
        if i * j > K:
            break
        m[i] -= m[i*j]
        j += 1

ans = 0
for i in range(1, K+1):
    ans = (ans + i * m[i]) % mod
print(ans)
