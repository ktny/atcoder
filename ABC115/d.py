import sys
sys.setrecursionlimit(500000)

N, X = map(int, input().split())

a, p = [1], [1]
for i in range(N):
    a.append(a[i] * 2 + 3)
    p.append(p[i] * 2 + 1)

def f(N, X):
    if N == 0:
        return 0 if X <= 0 else 1
    # Xがバンズ1枚とL-1バーガー1個分以下なら、
    # バンズ1枚を除いて(X-1)、L-1バーガーで同じ探索をするのと変わらない
    elif X <= 1 + a[N-1]:
        return f(N-1, X-1)
    # Xがバンズ1枚とL-1バーガー1個分より大きければ、
    # L-1バーガー1個分に入っているパティ + 1パティ+ Xを-2(一番下のバンズと真ん中のパティ)-(L-1バーガー1個分)で同じ探索をするのと変わらない
    else:
        return p[N-1] + 1 + f(N-1, X-2-a[N-1])

print(f(N, X))