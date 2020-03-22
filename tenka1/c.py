N = int(input())

from math import *

for h in range(1, 3501):
    for n in range(1, 3501):
        try:
            w = N*h*n / (4*h*n - N*n - N*h)
        except:
            continue
        if ceil(w) == floor(w) and w > 0:
            print(h, n, int(w))
            exit()
