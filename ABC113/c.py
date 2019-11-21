N, M = map(int, input().split())
PY = [tuple(map(int, input().split())) for i in range(M)]

py_map = {}
x = 1
prep = 0
for p, y in sorted(PY):
    if prep == p:
        x += 1
    else:
        x = 1
    py_map[(p,y)] = str(p).zfill(6) + str(x).zfill(6)
    prep = p

for p, y in PY:
    print(py_map[(p, y)])
