N, K = map(int, input().split())
A = list(map(int, input().split()))
# 実質1以外の数をK-1で何回で埋められるか
# ((N-1)+(K-1)-1) // (K-1)
print((N+K-3)//(K-1))
