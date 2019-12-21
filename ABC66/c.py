N = int(input())
A = list(map(int, input().split()))
A.reverse()

from collections import deque
b1 = deque([])
b2 = deque([])

for i in range(N):
    if i % 2 == 0:
        b1.append(A[i])
    else:
        b2.appendleft(A[i])
print(*(list(b1)+list(b2)))