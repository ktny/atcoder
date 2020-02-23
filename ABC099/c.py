from math import log
N = int(input())
dp = [0] * (10**5+1)
dpl = set()
a = 1
b = 1
while True:
    if a > 10**5:
        break
    a *= 6
    dpl.add(a)
while True:
    if b > 10**5:
        break
    b *= 9
    dpl.add(b)

for i in range(1, 10**5+1):
    if i < 6:
        dp[i] = i
        continue
    log6 = log(i, 6)
    log9 = log(i, 9)
    l = set(map(float, range(1, 20)))
    # 6の乗数、9の乗数の場合は1でdpを埋める
    if log6 in l:
        dp[i] = 1
    elif log9 in l:
        dp[i] = 1
    # それ以外の数値は各6, 9の乗数を引いた値から最も小さい数で埋める
    else:
        minl = [dp[i-d]+1 for d in dpl if i-d >= 0]
        if minl:
            dp[i] = min(minl)

print(dp[N])