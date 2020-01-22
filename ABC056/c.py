X = int(input())
a = 0
i = 1
while True:
    a += i
    if X <= a:
        break
    i += 1
print(i)

# 1
# 2
# 3 1 2
# 4 1 3
# 5 2 3
# 6 1 2 3
# 7 1 2 4
# 8 1 3 4
# 9 2 3 4
# 10 1 2 3 4
# 11 1 2 3 5
# 12
# 13
# 14
# 15 1 2 3 4 5