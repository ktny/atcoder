N = int(input())
S = [list(input()) for i in range(N)]

for i in range(N-2, -1, -1):
    for j in range(1, N*2-2):
        if S[i][j] == '#' and (S[i+1][j-1] == 'X' or S[i+1][j] == 'X' or S[i+1][j+1] == 'X'):
            S[i][j] = 'X'

for i in range(N):
    print(*S[i], sep='')
