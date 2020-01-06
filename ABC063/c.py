N = int(input())
S = sorted([int(input()) for i in range(N)])
min_no_ten = float('inf')
for s in S:
    if s % 10 != 0:
        min_no_ten = s
        break
else:
    print(0)
    exit()

total = sum(S)
if total % 10 != 0:
    print(total)
else:
    print(total - min_no_ten)
