N = int(input())
F = [''.join(input().split()) for i in range(N)]
P = [list(map(int, input().split())) for i in range(N)]

ans = -1 * float('inf')
for i in range(1, 2**10):
    tmp = 0
    for j in range(N):
        product = i & int(F[j], base=2)
        c = bin(product).count('1')
        tmp += P[j][c]
    ans = max(ans, tmp)

print(ans)