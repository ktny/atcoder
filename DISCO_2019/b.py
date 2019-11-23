N = int(input())
# 四等分した1つの正方形だけ考えると、
# 2等分すると1
# 3等分すると1+2
# 4等分すると1+2+3...と等差数列で増えていくことがわかる
base = sum(range(N//2))*4
if N % 2 == 0:
    print(base)
else:
    print(base+1)