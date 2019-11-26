from itertools import product
N = int(input())
d = len(str(N))
ans = []
# 重複順列組み合わせで最大でも3**10の組み合わせを超えないので全探索ができる
for i in range(3, d+1):
    cs = product([3,5,7], repeat=i)
    for c in cs:
        if set(c) == {3, 5, 7}:
            if i < d or (i == d and int(''.join(map(str, c))) <= N):
                ans.append(c)
print(len(ans))
