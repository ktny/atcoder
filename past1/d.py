N = int(input())
A = [int(input()) for i in range(N)]
from collections import Counter
c = Counter(A)
before = 0
after = 0
for i in range(1, N+1):
    if c[i] == 2:
        after = i
    elif c[i] == 0:
        before = i
if before == after == 0:
    print('Correct')
else:
    print(after, before)