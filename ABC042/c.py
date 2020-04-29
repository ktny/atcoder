N, K = map(int, input().split())
D = set(list(map(str, input().split())))

for i in range(N, 10**6):
    if N <= i and len(set(str(i)) & D) == 0:
        print(i)
        exit()