N = int(input())
S = list(input())
ws = [0]*N
es = [0]*N
# 自分より前のWと自分より後のEの数だけ振り向かせる
for i in range(N-1):
    if S[i] == 'W':
        ws[i+1] += ws[i]+1
    else:
        ws[i+1] = ws[i]
for i in range(N-1, 0, -1):
    if S[i] == 'E':
        es[i-1] += es[i]+1
    else:
        es[i-1] = es[i]
ans = []
for w, e in zip(ws, es):
    ans.append(w+e)
print(min(ans))