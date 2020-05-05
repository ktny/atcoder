N, K, C = map(int, input().split())
S = input()

# 前から貪欲に働く日を決めていく。一番早く働く場合
L = []
L_l = 0
off = 0
for i in range(N):
    if S[i] == 'o' and off <= 0:
        L.append(i)
        L_l += 1
        if L_l == K:
            break
        off = C
    else:
        off -= 1

# 後ろから貪欲に働く日を決めていく。一番遅く働く場合
R = []
R_l = 0
off = 0
for i in range(N-1, -1, -1):
    if S[i] == 'o' and off <= 0:
        R.append(i)
        R_l += 1
        if R_l == K:
            break
        off = C
    else:
        off -= 1
R.sort()

# 一番早く働いても遅く働いてもi番目に働く日が同じになる場合、その日は必ず働く必要がある
ans = []
for i in range(K):
    if L[i] == R[i]:
        ans.append(L[i]+1)
print(*ans, sep='\n')
