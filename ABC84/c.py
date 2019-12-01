N = int(input())
CSF = [list(map(int, input().split())) for i in range(N-1)]
for i in range(N-1):
    ans = 0
    for j in range(i, N-1):
        C, S, F = CSF[j]
        if ans < S:
            ans = S
        else:
            diff = ans - S
            if diff % F != 0:
                ans += F - (diff % F)
        ans += C
    print(ans)
print(0)
