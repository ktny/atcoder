M, D = map(int, input().split())

ans = 0
for m in range(1, M+1):
    for d in range(1, D+1):
        d10, d1 = divmod(d, 10)
        if d10 >= 2 and d1 >= 2 and d10 * d1 == m:
            ans += 1
print(ans)