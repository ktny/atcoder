N = int(input())
P = []

def is_prime(n: int):
    if n == 2:
        return True
    if n == 1 or n % 2 == 0:
        return False
    for p in range(3, int(n**0.5)+1, 2):
        if n % p == 0:
            return False
    return True

for i in range(5, 55555+1):
    # 素数かつ5で割って1余る数を列挙する
    # 5で割って1余る数だけならどれを5を選んでも5で割り切れる合成数になるから
    if is_prime(i) and i % 5 == 1:
        P.append(i)

print(*P[:N])