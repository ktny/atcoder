N = int(input())
A = list(map(int, input().split()))

fours = 0
twos = 0
ones = 0
for i in range(N):
    if A[i] % 4 == 0:
        fours += 1
    elif A[i] % 2 == 0:
        twos += 1
    else:
        ones += 1

if twos:
    ones += 1

if ones <= fours + 1:
    print('Yes')
else:
    print('No')
 