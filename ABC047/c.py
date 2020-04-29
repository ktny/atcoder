s = input()

pre = s[0]
ans = 0
for i in range(1, len(s)):
    if pre != s[i]:
        ans += 1
        pre = s[i]

print(ans)