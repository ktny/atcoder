S = input()
N = len(S)

words = []
mode = False
tmp = []
for i in range(N):
    tmp.append(S[i].lower())
    if S[i].isupper():
        if mode:
            words.append(''.join(tmp))
            tmp = []
            mode = False
        else:
            mode = True

ans = []
for w in sorted(words):
    l = len(w)
    for i, c in enumerate(w):
        if i == 0 or i == l-1:
            ans.append(c.upper())
        else:
            ans.append(c)
print(*ans, sep='')

# print(words)
# print(sorted(ans))
# print(''.join(sorted(ans)))