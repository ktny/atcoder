N, M = map(int, input().split())

# 奇数のときは最後の数だけを最初に飛ばした形で先頭、末尾から作っていけばok
if N % 2 == 1:
    for i in range(1, M+1):
        print(i, N-i)
# 偶数のときは奇数と同じように作ると対戦距離がNの半分になるものがあるので一周したときに重複する
# 対戦距離がNの半分になるものが出ないように、対戦距離が半分になった時点で1つずらす
# 対戦距離 = b - a
else:
    for i in range(1, M+1):
        if N-2*i <= N//2:
            print(i, N-i-1)
        else:
            print(i, N-i)