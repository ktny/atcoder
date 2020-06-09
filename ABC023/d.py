N = int(input())
HS = [list(map(int, input().split())) for i in range(N)]

left, right = 0, 10**15
while right > left+1:
    mid = (left + right) // 2
    # 各風船を何秒後までに割ればいいか。ソートしてそのインデックスの秒後に割るのがまにあわない場合はmidが間違ってる
    time = sorted([(mid-h)/s for h, s in HS])
    # すべて間に合う場合はmidをもっと下げられる
    flag = all([True if time[i] >= i else False for i in range(N)])
    if flag:
        right = mid
    else:
        left = mid

print(right)
