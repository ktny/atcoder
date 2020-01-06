N = int(input())
A = list(map(int, input().split()))
B = sorted([A[i]-(i+1) for i in range(N)])
b = B[N//2]
print(sum([abs(B[i]-b) for i in range(N)]))