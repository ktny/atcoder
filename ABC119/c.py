import sys
sys.setrecursionlimit(500000)

N, A, B, C = map(int, input().split())
L = [int(input()) for i in range(N)]

kumi = []
abcx = ['A', 'B', 'C', 'X']

def dfs(arr: list):
    if len(arr) == N:
        kumi.append(arr[:])
        return
    for k in ['A', 'B', 'C', 'X']:
        arr.append(k)
        dfs(arr)
        arr.pop()

dfs([])

ans = float('inf')
for k in kumi:
    if set(k) & set(['A', 'B', 'C']) != set(['A', 'B', 'C']):
        continue
    tmp = 0
    a = 0
    b = 0
    c = 0
    for i in range(N):
        if k[i] == 'A':
            if a > 0:
                tmp += 10
            a += L[i]
        elif k[i] == 'B':
            if b > 0:
                tmp += 10
            b += L[i]
        elif k[i] == 'C':
            if c > 0:
                tmp += 10
            c += L[i]
    tmp += abs(A-a)
    tmp += abs(B-b)
    tmp += abs(C-c)
    ans = min(ans, tmp)

print(ans)