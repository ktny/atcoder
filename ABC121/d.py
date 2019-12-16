A, B = map(int, input().split())

def f(n, k):
    if n < 0:
        return 0
    if n // 2**k == 0:
        if n >= 2**(k-1):
            return n - 2**(k-1) + 1
        else:
            return 0
    else:
        return int((n // 2**k) * (2**(k-1))) + f(n-(n // 2**k)*(2**k), k)

ans = []
for k in range(1, len(bin(10**12))-1):
    b = f(B, k)
    a = f(A-1, k)
    one = b-a
    if one % 2 == 0:
        ans += '0'
    else:
        ans += '1'

ans.reverse()
print(int(''.join(ans), 2))