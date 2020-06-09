from math import floor, ceil
H, W = map(int, input().split())

ans = float('inf')
for h in range(1, H+1):
    A = h * W
    B = floor((H-h) / 2) * W
    C = ceil((H-h) / 2) * W
    B2 = (H-h) * floor(W / 2)
    C2 = (H-h) * ceil(W / 2)
    ans = min(ans, max([A, B, C]) - min([A, B, C]))
    ans = min(ans, max([A, B2, C2]) - min([A, B2, C2]))

for w in range(1, W+1):
    A = H * w
    B = floor((W-w) / 2) * H
    C = ceil((W-w) / 2) * H
    B2 = (W-w) * floor(H / 2)
    C2 = (W-w) * ceil(H / 2)
    ans = min(ans, max([A, B, C]) - min([A, B, C]))
    ans = min(ans, max([A, B2, C2]) - min([A, B2, C2]))

print(ans)