N = int(input())
H = list(map(int, input().split()))

# 0から考えるのではなく、一番高い花を1つずつ減らして均していっても同じ回数になる
# さらに考えると、左から考えて隣より高さ分減らせばいいからO(N)で求まる
ans = 0
for i in range(N):
    if i == N-1:
        ans += H[i]
    elif H[i] > H[i+1]:
        ans += H[i] - H[i+1]
print(ans)