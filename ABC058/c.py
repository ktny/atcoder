N = int(input())
S = [sorted(input()) for i in range(N)]

from collections import Counter

common = Counter(S[0])
for i in range(1, N):
    c = Counter(S[i])
    dels = []
    for char, count in common.items():
        if char in c:
            if c[char] < count:
                common[char] = c[char]
        else:
            dels.append(char)
    for d in dels:
        del common[d]

ans = []
for k, v in common.items():
    ans.append(k * v)
print(''.join(sorted(ans)))

