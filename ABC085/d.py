N, H = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(N)]

max_a = sorted(ab, key=lambda x: -x[0])[0][0]
bs = sorted([b for a,b in ab if b > max_a], reverse=True)
sum_bs = sum(bs)

if H <= sum_bs:
    for i in range(len(bs)):
        H -= bs[i]
        if H <= 0:
            print(i+1)
            exit()
else:
    H -= sum_bs
    print((H+max_a-1)//max_a + len(bs))
