N = int(input())
A = list(map(int, input().split()))

conds = [400*i for i in range(1,9)]
colors = set()
frees = 0
for i in range(N):
    for c in conds:
        if A[i] < c:
            colors.add(c)
            break
    else:
        frees += 1
clen = len(colors)
print(clen if clen else 1, clen+frees)
