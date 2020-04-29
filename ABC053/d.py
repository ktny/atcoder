N = int(input())
A = list(map(int, input().split()))
c = len(set(A))
print(c-1 if c % 2 == 0 else c)