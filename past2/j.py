S = input()
N = len(S)

ans = []
tmp = [[] for _ in range(N)]
kakko = 0
for i in range(N):
    c = S[i]
    if c == ')':
        tmp[kakko] += reversed(tmp[kakko])
        kakko -= 1
        tmp[kakko].append(''.join(tmp[kakko+1]))
        tmp[kakko+1] = []
    elif c == '(':
        kakko += 1
    else:
        tmp[kakko].append(c)
    if kakko == 0:
        ans.append(''.join(tmp[0]))
        tmp[0] = []

print(''.join(ans))