N, M = map(int, input().split())
LR = sorted([list(map(int, input().split())) for i in range(M)], key=lambda x: (x[0], -x[1]))
 
minv = 0
maxv = N
for l, r in LR:
    if maxv < l:
        print(0)
        exit()
    minv = max(minv, l)
    maxv = min(maxv, r)
 
print(maxv-minv+1)