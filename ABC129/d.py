H, W = map(int, input().split())
rows = [input() for i in range(H)]
cols = []
for i in range(W):
    col = ''
    for row in rows:
        col += row[i]
    cols.append(col)

rowmap = []

# ans = 0
# for h in range(H):
#     for w in range(W):
#         if rows[h][w] == '#':
#             continue
#         rows[h].find('#', start=)