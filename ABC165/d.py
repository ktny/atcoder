A, B, N = map(int, input().split())

# from math import floor
# floor(A*x/B) - A*floor(x/B)
# (A*x-x%B) - A*(x-x%B)
# A*x - x%B - A*x + A*(x%B)
# x%B + A*(x%B)
# Aは定数なので x%B を最大化すればよい
# x%Bを最大化するにはxは基本的にはB-1
# NがB-1を取り得ない場合はN

x = B-1 if B-1 <= N else N
print(A*x//B - A*(x//B))