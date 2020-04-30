N = int(input())
S1 = input()
S2 = input()
mod = 10**9+7

ans = 1
pre = None
i = 0
while i < N:
    if pre is None:
        if S1[i] == S2[i]:
            ans = ans*3 % mod
            pre = 'x'
            i += 1
        else:
            ans = ans*6 % mod
            pre = 'y'
            i += 2
    elif pre == 'x':
        if S1[i] == S2[i]:
            ans = ans*2 % mod
            pre = 'x'
            i += 1
        else:
            ans = ans*2 % mod
            pre = 'y'
            i += 2
    elif pre == 'y':
        if S1[i] == S2[i]:
            ans = ans*1 % mod
            pre = 'x'
            i += 1
        else:
            ans = ans*3 % mod
            pre = 'y'
            i += 2

print(ans % mod)