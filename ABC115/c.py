N, K = map(int, input().split())
H = sorted([int(input()) for i in range(N)], reverse=True)
ans = []
for i in range(N):
    try:
        ans.append(H[i] - H[i+K-1])
    except:
        pass
print(min(ans))