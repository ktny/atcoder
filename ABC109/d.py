H, W = map(int, input().split())
A = [list(map(int, input().split())) for i in range(H)]

ans = []
for i in range(H):
    if i % 2 == 0:
        start = 0
        end = W
        direction = 1
    else:
        start = W-1
        end = -1
        direction = -1
    for j in range(start, end, direction):    
        if A[i][j] % 2 == 0:
            continue
        else:
            if i % 2 == 0 and j < W-1:
                ans.append((i, j, i, j+1))
                A[i][j] -= 1
                A[i][j+1] += 1
            elif i % 2 == 0 and j == W-1 and i < H-1:
                ans.append((i, j, i+1, j))
                A[i][j] -= 1
                A[i+1][j] += 1
            elif i % 2 == 1 and j > 0:
                ans.append((i, j, i, j-1))
                A[i][j] -= 1
                A[i][j-1] += 1
            elif i % 2 == 1 and j == 0 and i < H-1:
                ans.append((i, j, i+1, j))
                A[i][j] -= 1
                A[i+1][j] += 1

# print(A)
print(len(ans))
for y,x,y2,x2 in ans:
    print(y+1,x+1,y2+1,x2+1)
