N, M = map(int, input().split())
AB = sorted([list(map(int, input().split())) for i in range(N)])
ans = 0
for a, b in AB:
    if M <= b:
        ans += a * M
        break
    else:
        ans += a * b
        M -= b
print(ans)