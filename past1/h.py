N = int(input())
C = list(map(int, input().split()))
Q = int(input())
SS = [list(map(int, input().split())) for i in range(Q)]

min_odd = min([c for i,c in enumerate(C, start=1) if i % 2 == 1])
min_all = min(C)
odd_sub_count = 0
all_sub_count = 0
ans = 0

for i in range(Q):
    S = SS[i]
    # print(i, S, ans, min_odd, min_all, odd_sub_count, all_sub_count)
    if S[0] == 1:
        x = S[1]
        a = S[2]
        if x % 2 == 0:
            if C[x-1] - all_sub_count < a:
                continue
            ans += a
            C[x-1] -= a
            min_all = min(min_all, C[x-1])
        else:
            if C[x-1] - odd_sub_count - all_sub_count < a:
                continue
            ans += a
            C[x-1] -= a
            min_odd = min(min_odd, C[x-1])
            min_all = min(min_all, C[x-1])
    elif S[0] == 2:
        a = S[1]
        if min_odd < a:
            continue
        ans += ((N+1)//2)*a
        min_odd -= a
        min_all = min(min_all, min_odd)
        odd_sub_count += a
    elif S[0] == 3:
        a = S[1]
        if min_all < a:
            continue
        ans += N*a
        min_all -= a
        min_odd -= a
        all_sub_count += a
print(ans)
