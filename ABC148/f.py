N, u, v = map(int, input().split())
G = [[] for i in range(N)]

for _ in range(N-1):
    A, B = map(int, input().split())
    G[A-1].append(B-1)
    G[B-1].append(A-1)

# 1つしかつながる頂点がないものを葉とする
isLeaf, dU, dV = [len(g) == 1 for g in G], [-1]*N, [-1]*N

for D, P in [(dU, u-1), (dV, v-1)]:
    S = [(P, 0)]
    while len(S) > 0:
        p, d = S.pop()
        D[p] = d # その頂点になんパスでいけるか記録
        # 今いる場所から行ける頂点がまだ行ったことのないところならキューに追加
        for g in G[p]:
            if D[g] == -1:
                S.append((g, d+1))

ans = 0
# 全頂点のうち、葉（端っこの頂点）であり、かつ、高橋くんの方が青木くんより先につける頂点のうち最大のものが2人が目指す頂点
# 最終的に高橋くんが自ら捕まりにいくので、その頂点1歩手前が答え
for i in range(N):
    if isLeaf[i] and dU[i] < dV[i]:
        ans = max(ans, dV[i]-1)

print(ans)
