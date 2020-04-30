N = int(input())
A = sorted(list(map(int, input().split())))

l = A[-1]
m = A[-1]//2
r = 0
tmp = 0
for i in range(N):
    d = min(abs(l-A[i]), abs(0-A[i]))
    if tmp < d:
        r = A[i]
        tmp = d

print(l, r)
