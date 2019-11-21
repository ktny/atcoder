N = int(input())
A = list(map(int, input().split()))
absa = [abs(a) for a in A]
m = 0
for a in A:
    if a < 0:
        m += 1
if m % 2 == 0:
    print(sum(absa))
else:
    print(sum(absa) - min(absa)*2)