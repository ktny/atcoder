H, W = map(int, input().split())

if H % 3 == 0 or W % 3 == 0:
    print(0)
elif H % 2 == 0 and W % 2 == 0:
    a = (H//2) * (W//2-1)
    b = H * W//2+1
    print(abs(a-b))
elif H % 2 == 0 and W % 2 != 0:
    a = (H//2) * (W//2)
    b = H * (W-(W//2))
    print(abs(a-b))
elif H % 2 != 0 and W % 2 == 0:
    a = (H//2) * (W//2)
    b = W * (H-(H//2))
    print(abs(a-b))
else:
    
    # a = (H//2) * (W//2)
    # b = H * (W-(W//2))
    # print(abs(a-b))
