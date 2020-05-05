N = int(input())

if N == 0:
    print(0)
    exit()

# 1桁目から見ていって奇数なら1があるはずなので1桁目は1とやっていく
ans = []
i = 1
while N:
    if N % 2 == 0:
        ans.append('0')
    else:
        ans.append('1')
        if i % 2 == 0:
            N += 1
        else:
            N -= 1
    N //= 2
    i += 1

zero = True
for b in reversed(ans):
    if zero and b == 0:
        continue
    elif b == 1:
        zero = False
    print(b, sep='', end='')
print()