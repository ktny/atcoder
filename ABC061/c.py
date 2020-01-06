N, K = map(int, input().split())
ab = sorted([list(map(int, input().split())) for i in range(N)])

for a, b in ab:
    K -= b
    if K <= 0:
        print(a)
        exit()
