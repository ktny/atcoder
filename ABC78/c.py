N, M = map(int, input().split())
# 1回の実行でかかる時間
x = 1900 * M + 100 * (N-M)
ans = 2**M * x
print(ans)