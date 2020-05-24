N = int(input())
TA = [list(map(int, input().split())) for i in range(N)]

t = 1
a = 1

for i in range(N):
    T, A = TA[i]
    if t > T or a > A:
        tmul = (t+T-1) // T
        amul = (a+A-1) // A
        mul = max(tmul, amul)
        T *= mul
        A *= mul
    t = T
    a = A
print(t+a)