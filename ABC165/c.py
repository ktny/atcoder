import sys
sys.setrecursionlimit(500000)
 
N, M, Q = map(int, input().split())
abcd = [list(map(int, input().split())) for i in range(Q)]
arr = []
 
def dfs(A: list):
    if len(A) == N:
        arr.append(A)
        return
    start = 1 if len(A) == 0 else A[-1]
    for i in range(start, M+1):
        dfs(A+[i])
 
dfs([])
 
ans = 0
for A in arr:
    tmp = 0
    for a,b,c,d in abcd:
        if A[b-1] - A[a-1] == c:
            tmp += d
    if ans < tmp:
        ans = tmp
print(ans)