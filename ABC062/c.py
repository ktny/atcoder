H, W = map(int, input().split())

if H % 3 == 0 or W % 3 == 0:
    print(0)


if H % 3 == 1 and W % 3 == 1:
    H // 3 * W 