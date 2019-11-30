N = int(input())
X = list(map(int, input().split()))

sx = sorted(X)
mid1 = sx[N//2-1]
mid2 = sx[N//2]

if mid1 == mid2:
    print(*[mid1]*N, sep='\n')
else:
    for i in range(N):
        if X[i] <= mid1:
            print(mid2)
        else:
            print(mid1)