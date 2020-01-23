N, M = map(int, input().split())
print(M // 2 if N >= M // 2 else N + (M-N*2)//4)