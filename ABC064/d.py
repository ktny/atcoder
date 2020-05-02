N = int(input())
S = input()
from collections import deque
q = deque([])

if S == '(' or S == ')':
    print('()')
    exit()

l = []
cnt = 0
for i in range(N-1):
    if S[i] == '(':
        cnt += 1
        if S[i+1] == ')':
            l.append(['a', cnt])
            cnt = 0
        elif S[i+1] == '(' and i+1 == N-1:
            l.append(['a', cnt+1])
            cnt = 0
    elif S[i] == ')':
        cnt += 1
        if S[i+1] == '(':
            l.append(['b', cnt])
            cnt = 0
        elif S[i+1] == ')' and i+1 == N-1:
            l.append(['b', cnt+1])
            cnt = 0

if S[-1] != S[-2]:
    if S[-1] == '(':
        if l[-1][0] == 'a':
            l[-1][1] += 1
        else:
            l.append(['a', 1])
    elif S[-1] == ')':
        if l[-1][0] == 'b':
            l[-1][1] += 1
        else:
            l.append(['b', 1])


a = 0
b = 0
for i in range(len(l)):
    k, c = l[i]
    if k == 'a':
        q.append('('*c)
        a += c
    if k == 'b':
        q.append(')'*c)
        b += c
        if a < b:
            q.appendleft('('*(b-a))
            a += (b-a)
if a > b:
    q.append(')'*(a-b))

print(*q, sep='')
