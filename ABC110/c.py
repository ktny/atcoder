S = input()
T = input()

from collections import Counter as c
s = c(S)
t = c(T)

if sorted(s.values()) == sorted(t.values()):
    print('Yes')
else:
    print('No')
