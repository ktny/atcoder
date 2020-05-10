import re
import sys
sys.setrecursionlimit(500000)
from string import ascii_lowercase
char = ascii_lowercase + '.'

S = input()
patterns = []
def dfs(n: int, A: list):
    if n == len(A):
        global patterns
        patterns.append(''.join(A))
        return
    for c in char:
        A.append(c)
        dfs(n, A)
        A.pop()

for i in range(1, 4):
    dfs(i, [])

ans = 0
for p in patterns:
    match = re.search(p, S)
    if match is not None:
        ans += 1

print(ans)