N = int(input())
A = list(map(int, input().split()))

from fractions import gcd
left = [A[0]]
right = [A[-1]]

# 左から順にgcdしたものと右から順にgcdしたものを前計算しておく
for i in range(1, N-1):
    left.append(gcd(left[-1], A[i]))
    right.append(gcd(right[-1], A[-1-i]))

ans = 1
for i in range(N):
    if i == 0:
        tmp = right[-1]
    elif i == N-1:
        tmp = left[-1]
    else:
        tmp = gcd(left[i-1], right[N-2-i])
    ans = max(ans, tmp)

print(ans)
