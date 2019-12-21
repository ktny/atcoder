N = int(input())
A = list(map(int, input().split()))
A.append(0)
# どこも飛ばさない場合にかかる金額
total = 0
cur = 0
for i in range(N+1):
    total += abs(A[i]-cur)
    cur = A[i]

cur = 0
for i in range(N):
    # 飛ばしたことにより金額が変わらない場合
    if (cur <= A[i] <= A[i+1]) or (A[i+1] <= A[i] <= cur):
        print(total)
    # 飛ばしたことにより金額が変わる場合（現時点が真ん中の場合）
    elif (A[i+1] <= cur <= A[i]) or (A[i] <= cur <= A[i+1]):
        print(total-abs(A[i]-cur)*2)
    # 飛ばしたことにより金額が変わる場合（現時点が真ん中でない場合）
    elif (A[i] <= A[i+1] <= cur) or (cur <= A[i+1] <= A[i]):
        print(total-abs(A[i+1]-A[i])*2)
    cur = A[i]
