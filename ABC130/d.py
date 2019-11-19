from bisect import bisect_right
N, K = map(int, input().split())
A = list(map(int, input().split()))
B = [0]
for i in range(N):
    B.append(B[i]+A[i])
ans = 0
# O(NlogN)でB[i]-K以上の個数をansに追加
for i in range(N+1):
    if K > B[i]:
        continue
    ans += bisect_right(B, B[i]-K)
print(ans)