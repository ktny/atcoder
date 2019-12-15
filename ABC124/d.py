N, K = map(int, input().split())
S = input()

zero = []
one = []
if S[0] == '0':
    one.append(0)
from itertools import groupby
for k, g in groupby(S):
    if k == '0':
        zero.append(len(list(g)))
    else:
        one.append(len(list(g)))
if S[-1] == '0':
    one.append(0)

if len(zero) <= K:
    print(N)
    exit()

zerob = [0]
oneb = [0]
for i in range(len(zero)):
    zerob.append(zerob[i] + zero[i])
for i in range(len(one)):
    oneb.append(oneb[i] + one[i])

ans = 0
for i in range(K, len(zerob)):
    z = zerob[i] - zerob[i-K]
    o = oneb[i+1] - oneb[i-K]
    ans = max(ans, z+o)

print(ans)
