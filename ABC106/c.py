S = input()
K = int(input())

ind = 0
ans = S[0]
for i in range(len(S)):
    if S[i] != '1':
        ind = i
        ans = S[i]
        break

if ind >= K:
    print(1)
else:
    print(ans)