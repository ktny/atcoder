Q = int(input())

from string import ascii_lowercase as al
from collections import deque
S = deque([])

for i in range(Q):
    query = input().split()
    if query[0] == '1':
        t,c,x = query
        S.append((c, int(x)))
    else:
        t,d = query
        d = int(d)
        tmp = {c:0 for c in al}
        while d and S:
            char, cnt = S.popleft()
            if d < cnt:
                cnt -= d
                tmp[char] += d
                d = 0
                S.appendleft((char, cnt))
            else:
                tmp[char] += cnt
                d -= cnt
        ans = 0
        for char, cnt in tmp.items():
            ans += cnt**2
        print(ans)

