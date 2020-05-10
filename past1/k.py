import sys
def input():
    return sys.stdin.readline()[:-1]

import sys
sys.setrecursionlimit(10**6)

N = int(input())
root = 0
tree = [[] for _ in range(N+1)]
for i in range(N):
    p = int(input())
    if p == -1:
        root = i+1
    else:
        tree[p].append(i+1)

vs = []
kukan = [[0]*2 for i in range(N+1)]

# 行きがけ順でnodeを記録していくことで各nodeが包含する区間がわかるようにする
def dfs(node: int, dep: int):
    vs.append(node)
    kukan[node][0] = len(vs)-1
    for to in tree[node]:
        dfs(to, dep+1)
    vs.append(node)
    kukan[node][1] = len(vs)-1

dfs(root, 0)

Q = int(input())
for i in range(Q):
    a, b = map(int, input().split())
    if kukan[b][0] <= kukan[a][0] <= kukan[b][1]:
        print('Yes')
    else:
        print('No')
