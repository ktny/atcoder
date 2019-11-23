N = int(input())
A = list(map(int, input().split()))
# 山1に降った量の半分をxと置くと、山2はA1-x、山3はA2-(A1-x)となり、翻って山1はA3-(A2-(A1-x))
# x = A3-A2+A1+x
# x = (A1+A3-A2) // 2
x = (sum(A[::2]) - sum(A[1::2])) // 2
ans = [x*2]
for i in range(N-1):
    a = A[i] - x
    ans.append(a*2)
    x = a
print(*ans)